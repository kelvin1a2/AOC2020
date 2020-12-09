#!/usr/bin/python

def getNumbers():
    # Using readlines() 
    f = open('Day9\input.txt', 'r')
    return [int(x.strip()) for x in f.readlines()]

def findNumber(number, l_numbers):
    for index, item in enumerate(l_numbers):
        if sum(l_numbers[:(index+1)]) == number:
            print(f"Contiguous range found: smalles item {min(l_numbers[:(index+1)])} largest item {max(l_numbers[:(index+1)])}. Answergi = {min(l_numbers[:(index+1)]) + max(l_numbers[:(index+1)])}")
            return True
    return False
        

if __name__ == "__main__":
    l_numbers = getNumbers()
    i = 0 
    # 257342611
    while not findNumber(257342611, l_numbers[i:]):
        i+=1
    


