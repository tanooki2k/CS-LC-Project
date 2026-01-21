import asyncio
from time import sleep
from queue import Queue
from statistics import median
from threading import Thread
from random import uniform, randint


def get_median(lst):
    lst = sorted(lst)
    return median(lst)

def data_collector():
    while True:
        lst = queue.get()
        new_elem = get_median(lst)
        data.put(new_elem)

def data_printer():
    while True:
        elem = data.get()
        print(elem)

def generate_data():
    while True:
        for _ in range(randint(1, 10)):
            new_data = [uniform(20, 30) for _ in range(randint(15, 25))]
            queue.put(new_data)
        sleep(uniform(0.5, 2.5))


if __name__ == "__main__":
    queue = Queue()
    data = Queue()
    Thread(target=data_collector).start()
    Thread(target=data_printer).start()
    generate_data()

