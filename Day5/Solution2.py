#!/usr/bin/python
import math

def readFile():
    # Using readlines() 
    file1 = open("input.txt", 'r') 
    Lines = file1.readlines() 
    return Lines

def calculateRow(row):
    rows = 128
    currentRow = [0, 127]
    j = 1
    for i in row:
        if i == 'F':
            currentRow[1] -= rows >> j
        elif i == "B":
            currentRow[0] += rows >> j
        else:
            print(f"wrong letter {i}")
        j += 1
    if currentRow[0] == currentRow[1]:
        # print(f"CurrentRow: {currentRow}")
        pass
    else:
        print(f"Error CurrentRow: {currentRow}")
    return currentRow[0]

def calculateColumn(column):
    columns = 8
    currentColumn = [0, 7]
    j = 1
    for i in column:
        if i == 'L':
            currentColumn[1] -= columns >> j
        elif i == "R":
            currentColumn[0] += columns >> j
        else:
            print(f"wrong letter {i}")
        j += 1
    if currentColumn[0] == currentColumn[1]:
        # print(f"currentColumn: {currentColumn}")
        pass
    else:
        print(f"ERROR currentColumn: {currentColumn}")
    return currentColumn[0]

if __name__ == "__main__":
    seats = readFile()
    highestSeadId = 0
    l_seatid = list()
    # print(seats)
    for seat in seats:
        if seat[-1:] == '\n':
            seat = seat[:10]
        column = seat[-3:]
        row = seat[:7]
        rowNumber = calculateRow(row)
        columnNumber = calculateColumn(column)
        seatID = (rowNumber*8) + columnNumber
        l_seatid.append(seatID)
        if seatID > highestSeadId:
            highestSeadId = seatID
        # print(f"{seat}: row {rowNumber}, column {columnNumber}, seat ID {seatID}")
    # print(f"Hightest Seatid {highestSeadId}")
    # seat = 'FBFBBFFRLR'
    l_seatid.sort()
    # print('aaa')
    last_seatid = 95
    for currentID in l_seatid:
        if abs(currentID-last_seatid) > 1:
            print(f"last id: {last_seatid} and current id: {currentID} makes seat: {currentID-1}")
        last_seatid = currentID

