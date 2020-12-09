#!/usr/bin/python
import re

def getNumbers():
    # Using readlines() 
    f = open('Day9\input.txt', 'r')
    return [int(x.strip()) for x in f.readlines()]

def calcValidNumber(number, index, preamble, l_numbers):
    # print(number)
    valid = False
    for i in l_numbers:
         for j in l_numbers:
            if number == (i+j):
                valid = True
    if not valid:
        print(f"number {number}")
    return valid

if __name__ == "__main__":
    l_numbers = getNumbers()
    i = 0 
    preamble = 25
    while calcValidNumber(l_numbers[preamble], 0, preamble, l_numbers[i:preamble]):
        i+=1
        preamble+=1


