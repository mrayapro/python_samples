import time
import random

def heavyduty():
    time.sleep(random.randint(1,5))

heavyduty()
print(time.time())

def timer(f):
    def wrapper():
            s = time.time()
            f()
            e = time.time()
            print("Took", e-s , "seconds")
    return wrapper
@timer
