import random
import time
from dataclasses import dataclass
from typing import Any

from otherstuff import f1


@dataclass
class D:
    data: Any = None


d = D()


def f2():
    while True:
        time.sleep(0.5)
        print(d.data)


from threading import Thread

Thread(target=f1, args=(d,)).start()

if __name__ == "__main__":
    f2()
