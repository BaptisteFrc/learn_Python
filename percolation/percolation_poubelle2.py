from random import randint
from time import time
import sys

start_time = time()

size = int(sys.argv[2])
length = size * size
grid = []
equiv = []

def init():
    global grid
    global equiv
    grid = [False for _ in range(length)]
    equiv = [i for i in range(length)]




