#!/usr/bin/python

NORTH, SOUTH, WEST, EAST, LEFT, RIGHT, FORWARD = 'NSWELRF'

def readFile():
    return [x for x in open('Day12/input.txt').read().splitlines()]

def calcAbsdiff(l_file):
    x = 0
    y = 0
    dx = 10  
    dy = 1  
    for instruction in l_file:
        pos = instruction[0]
        value = int(instruction[1:])
        if pos == NORTH:
            dy += value
        elif pos == SOUTH:
            dy -= value
        elif pos == EAST:
            dx += value
        elif pos == WEST:
            dx -= value
        elif pos == LEFT:
            for i in range(value//90):
                dx, dy = -dy, dx
        elif pos == RIGHT:
            for i in range(value//90):
                dx, dy = dy, -dx
        elif pos == FORWARD:
            x += value * dx
            y += value * dy
    return x,y

if __name__ == "__main__":
    l_file = readFile()
    answer = calcAbsdiff(l_file)
    print(f'Answer: {abs(answer[0]) + abs(answer[1])}')
 
    