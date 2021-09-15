import time

def inc(x):
    time.sleep(0.5)
    return x + 1

def double(x):
    time.sleep(0.5)
    return 2 * x

def add(x, y):
    time.sleep(0.5)
    return x + y

data = list(range(10))

output = []
for x in data:
    a = client.submit(inc, x)
    b = client.submit(double, x)
    c = client.submit(add, a, b)
    output.append(c)

total = client.submit(sum, output)
total.result()