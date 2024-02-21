import timeit
from typing import Dict
from itertools import chain

# Define the dictionaries
d1: Dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}


# Define a function for each method
def method1(d1, d2):
    return d1 | d2


def method2(d1, d2):
    d = d1.copy()
    d.update(d2)
    return d


def method3(d1, d2):
    return dict(d1, **d2)


def method4(d1, d2):
    return dict(chain(d1.items(), d2.items()))


# List of methods
methods = [method1, method2, method3, method4]

# Measure the time taken by each method
for i, method in enumerate(methods, start=1):
    start_time = timeit.default_timer()
    d = method(d1, d2)
    time_taken = timeit.default_timer() - start_time
    print(f'Method {i}:', d)
    print(f'Time Taken by Method {i}:', time_taken)
