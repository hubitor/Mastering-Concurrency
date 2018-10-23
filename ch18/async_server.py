import socket, select, types
from collections import namedtuple

###########################################################################
# Reactor

Session = namedtuple('Session', ['address', 'file'])

sessions = {}           # { csocket : Session(address, file)}
callback = {}           # { csocket : callback(client, line) }
generators = {}         # { csocket : inline callback generator }

# Main event loop
def reactor(host='localhost', port=9600):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    sock.setblocking(0) # Make asynchronous
    sessions[sock] = None
    print(f'Server up, running, and waiting for call on {host} {port}.')

    try:
        while True:
            # Serve existing clients only if they already have data ready
            ready_to_read, _, _ = select.select(sessions, [], [], 0.1)
            for conn in ready_to_read:
                if conn is sock:
                    conn, cli_address = sock.accept()
                    connect(conn, cli_address)
                    continue

                line = sessions[conn].file.readline()
                if line:
                    callback[conn](conn, line.rstrip())
                else:
                    disconnect(conn)

    finally:
        sock.close()

def connect(conn, cli_address):
    sessions[conn] = Session(cli_address, conn.makefile())

    gen = process_request(conn)
    generators[conn] = gen

    callback[conn] = gen.send(None) # Starting the generator

def disconnect(conn):
    # Cleaning conn from dictionaries
    gen = generators.pop(conn)
    gen.close()
    sessions[conn].file.close()
    conn.close()

    del sessions[conn]
    del callback[conn]

@types.coroutine
def readline(conn):
    def inner(conn, line):
        gen = generators[conn]
        try:
            callback[conn] = gen.send(line) # Continues the generator
        except StopIteration:
            disconnect(conn)

    line = yield inner
    return line

###########################################################################
# User's Business Logic

async def process_request(conn):
    mode = 'upper'
    print(f'Received connection from {sessions[conn].address}.')

    try:
        conn.sendall(b'<welcome: starting in upper case mode>\n')
        while True:
            line = await readline(conn)
            if line == 'quit':
                conn.sendall(b'connection closed\r\n')
                return
            if mode == 'upper' and line == 'title':
                conn.sendall(b'<switching to title case mode>\r\n')
                mode = 'title'
                continue
            if mode == 'title' and line == 'upper':
                conn.sendall(b'<switching to upper case mode>\r\n')
                mode = 'upper'
                continue

            print(f'{sessions[conn].address} --> {line}.')
            if mode == 'upper':
                conn.sendall(b'Upper-cased: %a\r\n' % line.upper())
            else:
                conn.sendall(b'Title-cased: %a\r\n' % line.title())
    finally:
        print(f'{sessions[conn].address} quit.')

if __name__ == '__main__':
    reactor('localhost', 8080)
