#!/usr/bin/python
import math

def readFile():
    # Using readlines() 
    return open("input.txt", 'r').readlines()

def getHeight(L_lines):
    return (len(L_lines) -1 )

def readPosition(line, rPosition):
    if line[(rPosition % len(line))] == "#":
        return True
    return False 


def makeStep(currentPosition):
    currentPosition[0:1] = currentPosition[0] + 1, currentPosition[1] + 3    
    return currentPosition

def countTrees(L_lines):
    currentPosition = [0,0]
    tree = 0
    while currentPosition[0] < getHeight(L_lines):
        currentPosition = makeStep(currentPosition)
        if readPosition(L_lines[currentPosition[0]][:-1], currentPosition[1]):
            tree +=1
    return tree

if __name__ == "__main__":
    print(countTrees(readFile()))


