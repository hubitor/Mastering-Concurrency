<div style="text-align:center">
<h1>
  <i>Mastering Concurrency in Python</i>:
  <br>
  A Brief Introduction
</h1>
</div>

<i>Immerse yourself in the world of Python concurrency and tackle the most complex concurrent programming problems</i>

<div style="text-align:center"><img align="center" src="https://d255esdrn735hr.cloudfront.net/sites/default/files/imagecache/ppv4_main_book_cover/B11327.png"/></div>

## Introduction
_Mastering Concurrency in Python_ will serve as a comprehensive introduction to various advanced concepts in concurrent engineering and programming in Python. This book will also provide a detailed overview of how concurrency and parallelism are being used in real-world applications. It is a perfect blend of theoretical analyses and practical examples, which will give you a full understanding of the theories and techniques regarding concurrent programming in Python.

More information on the book can be found below:
- Homepage: [_Mastering Concurrency in Python_](https://www.packtpub.com/application-development/mastering-concurrency-python)
- Author: [Quan Nguyen](https://github.com/KrisNguyen135)
- Publisher: [Packt Publishing Ltd](https://www.packtpub.com)

In this tutorial we will explore some fundamental concepts of concurrent programming, covered in _Mastering Concurrency in Python_. Specifically, we will see Python API that facilitates multithreading, multiprocessing, and asynchronous programming.

## Multithreading
Multithreading denotes the technique of creating and running multiple threads in a program at the same time. This can be achieved via the API of the `threading` module in Python. For example, say we have a function that will take a significant amount of time to run as follows:

```
import time

def sample_task(task_name):
    print(f'{task_name} starting...')
    time.sleep(2) # simulate processing time
    print(f'{task_name} finished.')
```

Now, we need to run this function multiple times in your Python program, and we can leverage the `threading` module to achieve that:

```
import threading

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
```

As we execute this sample program, we will obtain the following output:

```
Task 1 starting...
Task 2 starting...
Task 3 starting...
Task 1 finished.
Task 2 finished.
Task 3 finished.
```

The output indicates that the three threads were run simultaneously (as their printed output are in between each other). Multithreading is typically used when the tasks to be executed concurrently are relatively light-weight and do not excessively utilize the CPU. In _Mastering Concurrency in Python_, we explore the application of making web requests concurrently using multithreading. Specifically, we can design a ping test using the `requests` module:

```
import requests

def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.status_code}')
```

Now, we can concurrently loop through a set of websites that we'd like to ping using the `threading` module:

```
import threading

urls = [
    'http://www.python.org/',
    'http://www.packtpub.com/',
    'http://www.w3resource.com/',
    'http://www.python.org/psf/'
]

if __name__ == '__main__':
    threads = []
    for url in urls:
        thread = threading.Thread(target=ping, args=(url,))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
```

With the implementation of multithreading of light-weight tasks, significant improvement in execution time will be gained, in comparison to sequential programming. In _Mastering Concurrency in Python_, we also discuss the concept of queuing and other programming techniques commonly used with multithreading.

## Multiprocessing

The concept of multiprocessing is often used interchangeably with multithreading. Unlike multithreading, multiprocessing is about running multiple processes at the same time. For this reason, multiprocessing is typically applied when the tasks to be executed concurrently are heavy-weight. The cost of initializing processes to execute programming instructions is also higher than doing the same thing with threads, but it is more beneficial to apply multiprocessing to heavy-weight tasks in the long run.

Python provides similar API to facilitate multiprocessing as what we see above with multithreading via the `multiprocessing` module. Still considering the sample function that sleeps for 2 seconds above, we can execute it in multiple processes at the same time as follows:

```
import multiprocessing

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
```

Unlike in multithreading, a separate copy of the programming instructions is made when a process is initiated, and no pair of processes have shared memory or resources. For this reason, interprocess communication is a major element in multiprocessing programming. Furthermore, since it is quite expensive to run many processes at the same time, the strategy of creating a process to execute a run of a function (like what we did in the multithreading section) is not applicable anymore. Techniques regarding interprocess communication such as queues, joinable queues, or poison pills are discussed in details in _Mastering Concurrency in Python_.

## Asynchronous programming

Together with multithreading and multiprocessing, asynchronous programming is another major topic in concurrent programming. The technique involves task coordination through task switching. It is different from the other two techniques in the sense that the execution only takes place within one single thread in one single process.

The `asyncio` module, together with the keywords `async` and `await`, is the main tool to implement asynchronous programming in Python. We can execute multiple executions of the sample function above using asynchronous programming as follows:

```
import asyncio

async def async_sample_task(task_name):
    print(f'{task_name} starting...')
    await asyncio.sleep(2)
    print(f'{task_name} finished.')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(async_sample_task('Task 1')),
        loop.create_task(async_sample_task('Task 2')),
        loop.create_task(async_sample_task('Task 3'))
    ]

    loop.run_until_complete(asyncio.wait(tasks))

```

Note that to be asynchronously executed, a function would need to include the aforementioned keywords `async` and `await` to indicate that the function is a coroutine, a task to be executed in an asynchronous manner. Other important concepts such as event loops and futures are also included in the book.

## Other advanced topics
In addition to these three concurrent programming techniques and their usage from the Python language, _Mastering Concurrency in Python_ further explores the most common problems that engineers and programmers face while implementing concurrency: deadlock, starvation, and race condition. The book walks through the theoretical foundations and causes for each problem, analyzes and replicates them in Python programs, and finally discusses and implements potential solutions for each. The book also considers the infamous Global Interpreter Lock in Python and its role in the ecosystem of Python concurrent programming.

In the last section of the book, readers will be working on various advanced applications such as the design of lock-based and lock-free concurrent data structures, memory models and atomic operations, and building a concurrent server via low-level socket programming. The end of the book also covers the best practices when testing, debugging, and scheduling concurrent Python applications.

## Conclusion
If you have found this article interesting and would like to learn more about concurrent programming, you can find more information on _Mastering Concurrency in Python_ from [Packt](https://www.packtpub.com/application-development/mastering-concurrency-python) or [Amazon](https://www.amazon.com/dp/1789343054). Filled with both detailed theoretical analyses and hands-on examples, the book is an ideal resource for Python developers looking to leverage concurrency to improve their applications' speed and responsiveness.
