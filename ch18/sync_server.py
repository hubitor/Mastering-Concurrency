import socket
from collections import namedtuple

Session = namedtuple('Session', ['address', 'file'])
sessions = {}           # { csocket : Session(address, file) }

# Main event loop
def reactor(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    sessions[sock] = None
    print(f'Server up, running, and waiting for call on {host} {port}.')

    try:
        while True:
            conn, cli_address = sock.accept()
            sessions[conn] = Session(cli_address, conn.makefile())

            process_request(conn)

    finally:
        sock.close()

def process_request(conn):
    mode = 'upper'
    print(f'Received connection from {sessions[conn].address}.')

    try:
        conn.sendall(b'<welcome: starting in upper case mode>\n')
        while True:
            line = sessions[conn].file.readline()
            if line:
                line = line.rstrip()
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
        sessions[conn].file.close()
        del sessions[conn]
        conn.close()

if __name__ == '__main__':
    reactor('localhost', 8080)
