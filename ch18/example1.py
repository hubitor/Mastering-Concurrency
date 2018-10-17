# ch18/example1.py

import socket, time, types, select
from collections import namedtuple
from heapq import heappush, heappop

###########################################################################
# Reactor

scheduled_event = namedtuple('ScheduledEvent', ['event_time', 'task'])
session = namedtuple('Session', ['address', 'file'])

events = []
