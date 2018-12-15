import time
import multiprocessing

def sample_task(task_name):
    print(f'{task_name} starting...')
    time.sleep(2) # simulate processing time
    print(f'{task_name} finished.')

if __name__ == '__main__':
    # creating three processes, each runs the function once with unique parameter
    p1 = multiprocessing.Process(target=sample_task, args=('Task 1',))
    p2 = multiprocessing.Process(target=sample_task, args=('Task 2',))
    p3 = multiprocessing.Process(target=sample_task, args=('Task 3',))

    # starting the processes
    p1.start()
    p2.start()
    p3.start()

    # making sure all processes have finished
    p1.join()
    p2.join()
    p3.join()
