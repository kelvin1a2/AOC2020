#!/usr/bin/python
import re


# l = [int(x) for x in open('data/9.txt').read().splitlines()]

def getNumbers():
    return [int(x) for x in open('Day9/input.txt').read().splitlines()]

def findNumber(number, l_numbers):
    count = 0 
    for index, item in enumerate(l_numbers):
        count += item
        if count == number:
            print(f"Contiguous range found: smalles item {min(l_numbers[:(index+1)])} largest item {max(l_numbers[:(index+1)])}. Answergi = {min(l_numbers[:(index+1)]) + max(l_numbers[:(index+1)])}")
            return True
    return False
        

if __name__ == "__main__":
    l_numbers = getNumbers()
    i = 0 
    while not findNumber(257342611, l_numbers[i:]):
        i+=1
    


