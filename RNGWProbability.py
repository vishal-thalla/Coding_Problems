"""
You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""

import random
import msvcrt

def populate(probs, counts):
    
    return counts

arr = [20, 14, 78, 100, 21, 3, 51, 8]
probs = [0.13, 0.17, 0.1, 0.156, 0.2 ,0.144, 0.083, 0.017]

prefix = [probs[0]] # this array gives us probability ranges

for i in range(1, len(probs)):
    prefix.append(probs[i]+prefix[i-1])

counts = [0] *len(arr)
total = 0
while True:
    total +=1
    rng = random.random()
    i = 0
    while i < len(prefix)-1:
        if rng <= prefix[i]: break
        i +=1
    print(arr[i])
    counts[i] += 1

    if msvcrt.kbhit(): # this is just to display stats when user interrupts the Random Number generation
        for i in range(len(counts)):
            print(str(arr[i]) +': '+ str(float(counts[i])*100/total) + '%')
        break



