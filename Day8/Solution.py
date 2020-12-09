#!/usr/bin/python
import re

def getinstructions():
    # Using readlines() 
    f = open('Day8\input.txt', 'r')
    return [x.strip() for x in f.readlines()]

# accumulator = 0 

def doInstruction(l_instructions, currentInstruction,accumulator, currentIndex):
    action = currentInstruction.split(' ')[0]
    number = int(currentInstruction.split(' ')[1])
    # currentIndex = l_instructions.index(currentInstruction)
    if action == 'nop':
        currentIndex += 1
        return  [currentIndex, accumulator]
    if action == 'acc':
        accumulator += number
        currentIndex += 1
        return  [currentIndex, accumulator]
    if action == 'jmp':
        currentIndex += number
        print(f"currentIndex {currentIndex}")
        return  [currentIndex, accumulator]
    print("error")


if __name__ == "__main__":
    l_instructions = getinstructions()
    accumulator = 0 
    l_instructions_executed = list()
    i = 0 
    while i not in l_instructions_executed:
        # for instruction in l_instructions:
        # print(f"instruction: {instruction.split(' ')}")
        # print(accumulator)
        l_instructions_executed.append(i)
        returnValue = doInstruction(l_instructions, l_instructions[i],accumulator, i)
        currentInstruction = returnValue[0]
        accumulator = returnValue[1]
        # houdt index bij ipv instruction
        i = currentInstruction
    print(accumulator)
    # l_With_Bags = createBagsDict(l_infoBags)
    # recurseLookUpBag(l_With_Bags, 'shiny gold', list())
        


