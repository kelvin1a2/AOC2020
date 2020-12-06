#!/usr/bin/python
import math

def readFile():
    # Using readlines() 
    file1 = open("input.txt", 'r') 
    Lines = file1.readlines() 
    return Lines

def getWidth(L_lines):
    return len(L_lines[0][:-1])

def getHeight(L_lines):
    return (len(L_lines) -1 )

def readPosition(line, currentPosition, width): 
    if currentPosition[1] > width:
       stringMultiple = math.ceil(currentPosition[1] / width)
       stringMultiple += 1
       line = line * stringMultiple
    if line[currentPosition[1]] == "#":
        return True
    return False 


def makeStep(currentPosition):
    currentPosition[0] += 1
    currentPosition[1] += 3
    return currentPosition


if __name__ == "__main__":
    L_lines = readFile()
    width = getWidth(L_lines)
    height = getHeight(L_lines)
    currentPosition = [0,0]
    tree = 0
    i = 1
    while currentPosition[0] < height:
        currentPosition = makeStep(currentPosition)
        if readPosition(L_lines[i][:-1], currentPosition, width):
            tree +=1
        i +=1
    print(tree)


