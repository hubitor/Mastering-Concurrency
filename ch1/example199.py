from math import sqrt
import concurrent.futures
from timeit import default_timer as timer


limit = 1000000
sub_limit = int(sqrt(limit)) + 1



################################################################################

sieve = [True] * limit

for i in range(2, sub_limit):
    if sieve[i]:
        for j in range(i * 2, limit, i):
            sieve[j] = False

result =  [i for i in range(2, limit) if sieve[i]]
print('Result 1 length:')
print(len(result))



################################################################################

def process_sieve_v1(prime):
    global sieve

    for i in range(prime * 2, limit, prime):
        sieve[i] = False

sieve = [True] * limit

sub_limit = int(sqrt(limit)) + 1

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(process_sieve_v1, i) for i in range(2, sub_limit) if sieve[i]]

    _ = concurrent.futures.as_completed(futures)

result = [i for i in range(2, limit) if sieve[i]]
print('Result 2 length:')
print(len(result))



################################################################################

#def process_sieve_v2(i):
#    sieve[i] = False
