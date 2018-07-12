# statisticslib
Library for functions in statistics

#to find mean,mode,median of a given array
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))

#to lexicographically sort a string list



def staircase(n):
    for i in range(1, n +1):
        print (' ' * (n - i) + '#' * i)
