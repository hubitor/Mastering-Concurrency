from bad_linked_list import LinkedList

import threading
import time

def check_and_find(value):
    global my_linked_list

    if my_linked_list.check(value):
        time.sleep(1) # creating a delay
        # explain how result can be used for more important operations
        # so this can have more castatrophic results
        print(f'Index of {value}: {my_linked_list.find_index(value)}.')
        return

    print(f'Value {value} is not on the list.')

def check_and_delete(value):
    global my_linked_list

    if my_linked_list.check(value):
        time.sleep(1) # creating a delay
        my_linked_list.delete(value)

my_linked_list = LinkedList()
for i in range(10):
    my_linked_list.add(i)

thread1 = threading.Thread(target=check_and_delete, args=(0,))
thread2 = threading.Thread(target=check_and_delete, args=(2,))
thread3 = threading.Thread(target=check_and_find, args=(0,))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(f'Final linked list: {my_linked_list}.')
print('Finished.')
