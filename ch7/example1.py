# ch7/example1.py

from timeit import default_timer as timer
import multiprocessing


class ReductionConsumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    # TODO: either call task_done() on both numbers
    # or design the task queue differently to take
    # in two numbers in one job
    def run(self):
        pname = self.name
        #print('Using process %s...' % pname)

        while True:
            num1 = self.task_queue.get()
            if num1 is None:
                #print('Exiting process %s.' % pname)
                self.task_queue.task_done()
                break

            self.task_queue.task_done()
            num2 = self.task_queue.get()
            if num2 is None:
                #print('Reaching the end with process %s and number %i.' % (pname, num1))
                self.task_queue.task_done()
                self.result_queue.put(num1)
                break

            #print('Running process %s on numbers %i and %i.' % (pname, num1, num2))
            self.task_queue.task_done()
            self.result_queue.put(num1 + num2)


def built_in_sum(array):
    return sum(array)

def sequential_sum(array):
    running_sum = 0
    for item in array:
        running_sum += item

    return running_sum

def reduce_sum(array):
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.JoinableQueue()
    result_size = len(array)

    n_consumers = multiprocessing.cpu_count()

    for item in array:
        results.put(item)

    while result_size > 1:
        tasks = results
        results = multiprocessing.JoinableQueue()

        consumers = [ReductionConsumer(tasks, results) for i in range(n_consumers)]
        for consumer in consumers:
            consumer.start()

        for i in range(n_consumers):
            tasks.put(None)

        tasks.join()
        result_size = result_size // 2 + (result_size % 2)
        #print('-' * 40)

    return results.get()


power = 4
my_array = [i for i in range(10 ** power)]

start = timer()
result = built_in_sum(my_array)
print('Built-in function took %.2f seconds.' % (timer() - start))

start = timer()
result = sequential_sum(my_array)
print('Sequential function took %.2f seconds.' % (timer() - start))

start = timer()
result = reduce_sum(my_array)
print('Reduction operator took %.2f seconds.' % (timer() - start))
