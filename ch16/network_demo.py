from bad_network import Network as BadNetwork
from good_network import Network as GoodNetwork
import threading

def print_network_primary_value():
    global my_network

    print(f'Current primary value: {my_network.get_primary_value()}.')

my_network = BadNetwork('A', 1)
#my_network = GoodNetwork('A', 1)
print(f'Initial network: {my_network}')

my_network.add_node('B', 3)
my_network.add_node('C', 2)
print(f'Full network: {my_network}')

#print(my_network.get_primary_value())
#my_network.refresh_primary()
#print(f'Refreshed network: {my_network}')

thread1 = threading.Thread(target=print_network_primary_value)
thread2 = threading.Thread(target=my_network.refresh_primary)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Final network: {my_network}')
print('Finished.')
