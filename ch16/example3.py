# ch16/example3.py

import threading
from concurrent.futures import ThreadPoolExecutor
import time

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

for n_workers in range(1, 5):
    start = time.time()

    counter = LockedCounter()
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        executor.map(counter.increment, [1 for i in range(1000 * n_workers)])

    print(f'Final counter: {counter.get_value()}.')
    print(f'Number of threads: {n_workers}')
    print(f'Time taken: {time.time() - start : .2f} seconds.')
    print('-' * 40)
