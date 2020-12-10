#!/usr/bin/python
import re

def getJoltest():
    return [int(x) for x in open('Day10/input.txt').read().splitlines()]

# def checkList():


if __name__ == "__main__":
    l_joltes = getJoltest()
    l_joltes.sort()
    l_joltes.append(l_joltes[-1] + 3)
    jolt3= 1
    jolt1= 1
    for index, item in enumerate(l_joltes):
        if l_joltes[-1] == l_joltes[index+1]:
            print('last item reached {l_joltes[index]}')
            break
        else: 
            diff = l_joltes[index+1] - l_joltes[index]
            if diff == 3:
                jolt3 +=1
            elif diff == 1:
                jolt1 +=1
            else:
                print('hoit')
                print(f"diff: {diff}: l_joltes {l_joltes[index]} l_joltes + 1:  {l_joltes[index+1]}")
    print(f"jolt1 = {jolt1}")
    print(f"jolt3 = {jolt3}")
    print(f"answer = {jolt3*jolt1}")
