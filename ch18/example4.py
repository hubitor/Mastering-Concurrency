# ch18/example4.py

def read_data():
    for i in range(5):
        yield i * 2

result = read_data()
for i in range(6):
    print(next(result))
