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
    for i in range(-1,2):
        for j in range(-1,2):
            ## i,j == 0 is own seat
            seatRow = currentPos[0] + i
            seatCol = currentPos[1] + j
            if i == 0 and j == 0:
                continue
            #currentpos[0] is row ==i 
            #currentpos[1] is col == j
            elif seatRow < 0 or seatRow > maxRow:
                continue
            elif seatCol < 0 or seatCol > maxCol:
                continue
            elif l_file[seatRow][seatCol] == OCCUPIED:
                occupied_n +=1
    return occupied_n
             

def changeSeat(l_file,l_tmp_file):
    currentIndex = 0
    stateChanged = 0
    returnNumberOccupied = 0
    maxRow, maxCol = len(l_file) - 1, len(l_file[0]) - 1
    for indexRow, item in enumerate(l_file):
        for indexColumn, item in enumerate(l_file[indexRow]): 
            # print(f"indexColumn {currentIndex}, indexRow {indexRow}, {l_file[indexRow][indexColumn]}") 
            if indexColumn > maxCol or indexRow > maxRow:
                break
            occupied_n = calcOccupiedSeats(l_file, [indexRow, currentIndex], maxRow, maxCol)
            # print(f"empty seat, occupied {occupied_n}")
            if l_file[indexRow][currentIndex] == EMPTY and occupied_n == 0:
                # print(f"empty seat, occupied {occupied_n}")
                l_tmp_file[indexRow][currentIndex] = OCCUPIED
                stateChanged +=1
                # pass
            elif l_file[indexRow][currentIndex] == OCCUPIED and occupied_n >= 4:
                l_tmp_file[indexRow][currentIndex] = EMPTY
                stateChanged +=1 
                # pass
            else:
                #floor
                pass
            if l_file[indexRow][currentIndex] == OCCUPIED:
                returnNumberOccupied+=1
            currentIndex+=1
        currentIndex = 0
    # print2dlist(l_tmp_file)
    # print()
    return l_tmp_file, stateChanged, returnNumberOccupied

if __name__ == "__main__":
    l_file = readFile()
    # print(f"l_file {l_file[0][0]}")
    answer = (deepcopy(l_file), 1)
    # stateChanged = 1
    # answer.append(stateChanged)
    while answer[1] != 0:
        answer = changeSeat(answer[0], deepcopy(answer[0]))
        if answer[1] == 0:
            print(f'occupied {answer[2]}\n')   
        # print(f'stateChanged {answer[1]}\n')
        
