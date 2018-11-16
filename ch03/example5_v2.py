# ch3/example5.py

import queue
import threading
import time

exit = 0

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print('Starting thread %s.' % self.name)
        process_queue()
        print('Exiting thread %s.' % self.name)

def process_queue():
    while not exit:
        if not my_queue.empty():
            x = my_queue.get()
            print_factors(x)

        time.sleep(1)

def print_factors(x):
    result_string = 'Positive factors of %i are: ' % x
    for i in range(1, x + 1):
        if x % i == 0:
            result_string += str(i) + ' '
    result_string += '\n' + '_' * 20

    print(result_string)


# setting up variables
input = [1, 10, 4, 3]

my_queue = queue.Queue(10)


# initializing and starting 3 threads
thread1 = MyThread('A')
thread2 = MyThread('B')
thread3 = MyThread('C')

thread1.start()
thread2.start()
thread3.start()


# filling the queue
for x in input:
    my_queue.put(x)

# waiting for queue to empty
#while not my_queue.empty():
#    pass

# changing the flag exit so threads would stop
exit = 1

# joining all 3 threads
thread1.join()
thread2.join()
thread3.join()

print('Done.')
