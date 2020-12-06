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
    # print(f"new_line: {line}")
    new_line = line[:-1] 
    new_line += new_line
    if currentPosition[1] > width:
       #make width longer
       stringMultiple = math.ceil(currentPosition[1] / width)
       stringMultiple += 1
       new_line = new_line * stringMultiple
    # print(f"new_line: {new_line}")
    if new_line[currentPosition[1]] == "#":
        # print(f"currentPosition: {currentPosition}")
        # print(f"new_line: {new_line}")
        return True
    return False 

def makeStep(currentPosition, stepHeight, stepWidth):
    currentPosition[0] += stepHeight
    currentPosition[1] += stepWidth
    return currentPosition


if __name__ == "__main__":
    L_lines = readFile()
    width = getWidth(L_lines)
    height = getHeight(L_lines)
    currentPosition = [0,0]
    multipliedTrees = 1
    tree = 0
    paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    i =  paths[0][1]
    # paths = [[1,2]]
    for path in paths:
        # print(path)
        currentPosition = [0,0]
        tree = 0
        i = path[1]
        while currentPosition[0] < height:
            currentPosition = makeStep(currentPosition, path[1],path[0])
            if readPosition(L_lines[i], currentPosition, width):
                tree +=1
            i += path[1]
        print(f"Trees in {path} is: {tree}")
        multipliedTrees *= tree
    print(f"Answer is: {multipliedTrees}")
