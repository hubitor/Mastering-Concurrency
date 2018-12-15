import time
import threading

def sample_task(task_name):
    print(f'{task_name} starting...')
    time.sleep(2) # simulate processing time
    print(f'{task_name} finished.')

if __name__ == '__main__':
    # creating three threads, each runs the function once with unique parameter
    t1 = threading.Thread(target=sample_task, args=('Task 1',))
    t2 = threading.Thread(target=sample_task, args=('Task 2',))
    t3 = threading.Thread(target=sample_task, args=('Task 3',))

    # starting the threads
    t1.start()
    t2.start()
    t3.start()

    # making sure all threads have finished
    t1.join()
    t2.join()
    t3.join()
