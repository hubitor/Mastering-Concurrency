# ch16/example3.py

import threading
from concurrent.futures import ThreadPoolExecutor
import asyncio
import time

#import matplotlib.pyplot as plt

class LockedCounter():
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self, x):
        with self.lock:
            new_value = self.value + x
            time.sleep(0.001) # creating a delay
            self.value = new_value

    def get_value(self):
        with self.lock:
            value = self.value
        return value

#xs = []
#ys = []
for n_workers in range(1, 40):
    #print(n_workers)

    start = time.time()

    counter = LockedCounter()
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        executor.map(counter.increment, [1 for i in range(1000)])

    '''print(f'Final counter: {counter.get_value()}.')
    print(f'Number of threads: {n_workers}')
    print(f'Time taken: {time.time() - start : .2f} seconds.')
    print()'''
    print(f'{n_workers} threads: {time.time() - start : .2f} seconds.')

    #ys.append(time.time() - start)
    #xs.append(n_workers)

#plt.plot(xs, ys)
#plt.show()
