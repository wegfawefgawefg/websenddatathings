import random
import time


def f1(d):
    while True:
        time.sleep(0.2)
        d.data = random.randint(0, 100)
