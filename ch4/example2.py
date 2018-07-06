# ch4/example2.py

from threading import Lock


# induces deadlocks
def get_data_from_file_v1(filename):
    my_lock.acquire()

    with open(filename, 'r') as f:
        data.append(f.read())

    my_lock.release()

# handles exceptions
def get_data_from_file_v2(filename):
    with my_lock, open(filename, 'r') as f:
        data.append(f.read())


my_lock = Lock()
data = []

try:
    #get_data_from_file_v1('output2/sample0.txt')
    get_data_from_file_v2('output2/sample0.txt')
except:
    print('Encountered an exception...')

my_lock.acquire()
print('Lock acquired.')
