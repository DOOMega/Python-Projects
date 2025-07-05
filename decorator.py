from ast import arg
import math
import time

def decorator(func):
    def wrapper(x):
        print("before func func")
        func(x)
        print("after the func")
    return wrapper

@decorator
def thefunc(name):
    start = time.time()
    print("hello", name)
    finish = time.time()
    print(str(finish-start))
    

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print("fonksiyon "+func.__name__ + " " + str(finish - start) + "sürdü")
    return inner


@calculate_time
def us_alma(a,b):
    print(math.pow(a,b))
    
@calculate_time
def factoriel(num):
    print(math.factorial(num))


us_alma(5,2)
factoriel(5)
