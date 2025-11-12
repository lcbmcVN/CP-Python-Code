# '{:02d}'.format(1) --> 001
# '{0:.2f}'.format(1.5) --> 1.50
# (a/b)%c = (a mod (b * c) / b) mod c
# (a/b)%c = (a mod c * b^(c-2) mod c) mod c ||| c is prime number
# To use custom compare in heapq, make a Class have a __lt__ func

import sys,time,io
#from heapq import heapify, heappush, heappop
#from collections import defaultdict, deque, Counter, OrderedDict
#from math import gcd,log,log2,log10
#from bisect import bisect_left, bisect_right, insort_left, insort_right
#from typing import List, Tuple
#from functools import lru_cache, cmp_to_key

LOCAL = ''
def IO(name = ''):
    global LOCAL
    if name:
        LOCAL=name
        sys.stdin = open(name+'.inp', 'r')
        sys.stdout = open(name+'.out', 'w')

IO('task')

if LOCAL:
    raw_input = io.BytesIO(sys.stdin.buffer.read()).readline
    def input():
        return raw_input().decode().rstrip('\n')
else:
    input = lambda : sys.stdin.readline().rstrip('\n')

def printf(*args, sep = ' ', end = '\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#input = lambda : sys.stdin.buffer.readline().strip()
#input = BytesIO(read(0,fstat(0).st_size)).readline
#sys.setrecursionlimit(int(1e6))

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
        except SystemExit:
            end = time.time()
            if LOCAL:
                print(f'\n[Time taken: {end-start:.4f}s]', file = sys.stderr, flush = True)
            raise
        end = time.time()
        if LOCAL == 'task':
            print(f'\n[Time taken: {end-start:.4f}s]', file = sys.stderr, flush = True)
        return result
    return wrapper

# Constant
INF = 1<<60
MOD = int(1e9)+7
endl = '\n'

def solve():
    pass

@timed
def main():
    #Code
    t = int(input())
    for i in range(1,t+1):
        solve()

if __name__ == '__main__':
    main()
