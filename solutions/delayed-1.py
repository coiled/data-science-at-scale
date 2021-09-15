import time
from dask import delayed

@delayed
def inc(x):
    time.sleep(0.5)
    return x + 1

@delayed
def double(x):
    time.sleep(0.5)
    return 2 * x

@delayed
def add(x, y):
    time.sleep(0.5)
    return x + y

data = list(range(10))

output = []
for x in data:
    a = inc(x)
    b = double(x)
    c = add(a, b)
    output.append(c)

total = delayed(sum)(output)
%time total.compute()