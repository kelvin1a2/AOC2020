#!/usr/bin/python
import re

def getNumbers():
    # Using readlines() 
    f = open('Day9\input.txt', 'r')
    return [x.strip() for x in f.readlines()]

def findNumber(number, l_numbers):
    # print(number)
    valid = False
    count = 0 
    largest = 0
    smallest = l_numbers[0]
    i= 0
    for item in l_numbers:
        if int(item) == int(number):
            print("number must be at least two numbers")
            return False
        if int(item) > int(largest):
            largest = int(item)
        if int(item) < int(smallest):
            largest = int(item)
        count += int(item)
        if count == number:
            print(f"count {count}")
            print(f"l_numbers {l_numbers[:(i+1)]}")
            ints = [int(item) for item in l_numbers[:(i+1)]]
            ints.sort()
            print(f"number found: smalles item {ints[0]} largest item {ints[i]} = {ints[0]+ ints[i]}")
            return True
        if count > number:
            # print(f"count too big {count}")
            return False
        i += 1
    return valid
        

    # for i in l_numbers:
    #      for j in l_numbers:
    #         if int(number) == (int(i)+int(j)):
    #             # print('found: ' + i + ' en ' + j )
    #             valid = True
    #             # print('answer: ' + str(i*j))
    #             # exit()
    # if not valid:
    #     print(f"number {number}")
    # return valid

if __name__ == "__main__":
    l_numbers = getNumbers()
    number = 257342611
    i = 0 
    while not findNumber(number, l_numbers[i:]):
        i+=1
    
    # for i in range(currentIndex[0],currentIndex[1]):
    #     print(l_numbers[i])
        


