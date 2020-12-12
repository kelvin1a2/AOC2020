#!/usr/bin/python

OCCUPIED, EMPTY, FLOOR = '#L.'
from copy import deepcopy

def print2dlist(l_file):
    print('\n'.join(''.join(i) for i in l_file))

def readFile():
    f = open('day11\input.txt', 'r')
    return list(map(list, f.read().split('\n')))

def calcOccupiedSeats(l_file, currentPos, maxRow, maxCol):
    occupied_n = 0 
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for r, c in directions:
        dR, dC =  currentPos[0] + r,  currentPos[1] + c
        while (dR >= 0 and dR < len(l_file) and dC >= 0 and dC < len(l_file[0])):  
            if l_file[dR][dC] == OCCUPIED or l_file[dR][dC] == EMPTY or l_file[dR][dC] == FLOOR:
                if l_file[dR][dC] == OCCUPIED:
                    occupied_n += 1
                    break
            if l_file[dR][dC] == OCCUPIED or l_file[dR][dC] == EMPTY:
                break
            dR += r
            dC += c
    return occupied_n
             

def changeSeat(l_file,l_tmp_file):
    currentIndex = 0
    stateChanged = 0
    returnNumberOccupied = 0
    maxRow, maxCol = len(l_file) -1 , len(l_file[0]) -1 
    for indexRow, item in enumerate(l_file):
        for indexColumn, item in enumerate(l_file[indexRow]): 
            # print(f"indexColumn {currentIndex}, indexRow {indexRow}, {l_file[indexRow][indexColumn]}") 
            occupied_n = calcOccupiedSeats(l_file, [indexRow, currentIndex], maxRow, maxCol)
            # print(f"empty seat, occupied {occupied_n}")
            if l_file[indexRow][currentIndex] == EMPTY and occupied_n == 0:
                # print(f"empty seat, occupied {occupied_n}")
                l_tmp_file[indexRow][currentIndex] = OCCUPIED
                stateChanged +=1
                # pass
            elif l_file[indexRow][currentIndex] == OCCUPIED and occupied_n >= 5:
                l_tmp_file[indexRow][currentIndex] = EMPTY
                stateChanged +=1 
                # pass
            if l_file[indexRow][currentIndex] == OCCUPIED:
                returnNumberOccupied+=1
            currentIndex+=1
        currentIndex = 0
    # print2dlist(l_tmp_file)
    # print()
    return l_tmp_file, stateChanged, returnNumberOccupied

if __name__ == "__main__":
    l_file = readFile()
    answer = (deepcopy(l_file), 1)
    while answer[1] != 0:
        answer = changeSeat(answer[0], deepcopy(answer[0]))
        if answer[1] == 0:
            print(f'occupied {answer[2]}\n')   
        
