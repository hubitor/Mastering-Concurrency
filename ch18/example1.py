# ch18/example1.py

import socket, time, types, select
from collections import namedtuple
from heapq import heappush, heappop

###########################################################################
# Reactor

ScheduledEvent = namedtuple('ScheduledEvent', ['event_time', 'task'])
Session = namedtuple('Session', ['address', 'file'])

events = []             # heap with events prioritized by earliest time
sessions = {}           # { csocket : Session(address, file)}
callback = {}           # { csocket : callback(client, line) }
generators = {}         # { csocket : inline callback generator}

# Main event loop that triggers the appropriate business logic callbacks
def reactor(host='localhost', port=9600):
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    s.setblocking(0)    # Make asynchronous. Never wait on a client socket
    sessions[s] = None
    print(f'Server up, running, and waiting for call on {host} {port}.')

    try:
        while True:
            # Serve existing clients only if they already have data ready
            ready_to_read, _, _ = select.select(sessions, [], [], 0.1)
            for c in ready_to_read:
                if c is s:
                    c, a = c.accept()
                    connect(c, a)
                    continue

                line = sessions[c].file.readline()
                if line:
                    callback[c](c, line.rstrip())
                else:
                    disconnect(c)

            # Run events scheduled at the appropriate event time
            while events and events[0].event_time <= time.monotonic():
                event = heappop(events)
                event.task()

    finally:
        s.close()

# Reactor logic for new connections
def connect(c, a):
    sessions[c] = Session(a, c.makefile())
    on_connect(c)       # call into user's business logic

# Reactor logic to end sessions
def disconnect(c):
    on_disconnect(c)
    sessions[c].file.close()
    c.close()

    del sessions[c]
    del callback[c]

# Helper function to schedule one-time tasks at specific time
def add_task(event_time, task):
    heappush(events, ScheduledEvent(event_time, task))

# Helper function to schedule one-time tasks after a given delay
def call_later(delay, task):
    add_task(time.time() + delay, task)

# Helper function to schedule recurring tasks
def call_periodic(delay, interval, task):
    def inner():
        task()
        call_later(interval, inner)

    call_later(delay, inner)

def on_connect(c):
    g = nbcaser(c)      # `g` is a coroutine
    generators[c] = g   # generators -> awaitables
    callback[c] = g.send(None)  # we do this to advance `nbcaser` coroutine
                                # to yield through the `readline` coroutine
                                # which will sleep on its `yield` expression

def on_disconnect(c):
    g = generators.pop(c)
    g.close()

# A non-blocking readline to use with two-way generators
@types.coroutine
def readline(c):
    def inner(c, line):
        g = generators[c]
        try:
            callback[c] = g.send(line)  # `g.send(line)` will resume the
                                        # `yield inner` point
        except StopIteration:
            disconnect(c)

    line = yield inner
    return line

# A non-blocking sleep to use with two-way generators
def sleep(c, delay):
    def inner():
        g = generators[c]
        callback[c] = next(g)

    call_later(delay, inner)
    return lambda *args: callback[c]

###########################################################################
# User's Business Logic

def announcement():
    print(f'The event loop is still running at: {time.ctime()}.')

call_periodic(delay=1, interval=15, task=announcement)

async def nbcaser(c):
    upper, title = 'upper', 'title'
    mode = upper
    print(f'Received connection from {sessions[c].address}.')

    try:
        c.sendall(b'<welcome: starting in upper case mode>\n')
        while 1:
            line = await readline(c)
            if line == 'quit':
                c.sendall(b'quit\r\n')
                return
            if mode is upper and line == 'title':
                c.sendall(b'<switching to title case mode>\r\n')
                mode = title
                continue
            if mode is title and line == 'upper':
                c.sendall(b'<switching to upper case mode>\r\n')
                mode = upper
                continue

            print(f'{sessions[c].address} --> {line}.')
            if mode is upper:
                c.sendall(b'Upper-cased: %a\r\n' % line.upper())
            else:
                c.sendall(b'Title-cased: %a\r\n' % line.title())

    finally:
        print(f'{sessions[c].address} quit.')

if __name__ == '__main__':
    reactor('localhost', 9600)
