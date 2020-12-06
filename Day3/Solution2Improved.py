#!/usr/bin/python
import math

def readFile():
    # Using readlines() 
    return open("input.txt", 'r').readlines()

def getHeight(L_lines):
    return (len(L_lines) -1 )

def readPosition(line, currentPosition):
    if line[(currentPosition[1] % len(line))] == "#":
        return True
    return False 

def makeStep(currentPosition, stepHeight, stepWidth):
    currentPosition[0] += stepHeight
    currentPosition[1] += stepWidth
    return currentPosition


if __name__ == "__main__":
    L_lines = readFile()
    height = getHeight(L_lines)
    currentPosition = [0,0]
    multipliedTrees = 1
    tree = 0
    paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    # paths = [[1,2]]
    for path in paths:
        # print(path)
        currentPosition = [0,0]
        tree = 0
        while currentPosition[0] < height:
            currentPosition = makeStep(currentPosition, path[1],path[0])
            if readPosition(L_lines[currentPosition[0]][:-1], currentPosition):
                tree +=1
        print(f"Trees in {path} is: {tree}")
        multipliedTrees *= tree
    print(f"Answer is: {multipliedTrees}")
