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

In this tutorial we will explore some fundamental concepts of concurrent programming, covered in _Mastering Concurrency in Python_. Specifically, we will see Python API that facilitates multithreading, multiprocessing, and asynchronous programming. For each of those techniques we will also consider specific applications that will benefit from concurrency in Python.

## Multithreading
Multithreading denotes the technique of creating and running multiple threads in a program at the same time. This can be achieved via the API of the `threading` module in Python. For example, say we have a function that will take a significant amount of time to run as follows:

```
import time

def threading_sample_task(task_name):
    print(f'{task_name} starting...')
    time.sleep(2) # simulate processing time
    print(f'{task_name} finished.')
```

Now, we need to run this function multiple times in your Python program, and we can leverage the `threading` module to achieve that:

```
import threading

# creating three threads, each runs the function once with unique parameter
t1 = threading.Thread(target=threading_sample_task, args=('Task 1',))
t2 = threading.Thread(target=threading_sample_task, args=('Task 2',))
t3 = threading.Thread(target=threading_sample_task, args=('Task 3',))

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
```
