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
        # print(f"currentIndex {currentIndex}")
        return  [currentIndex, accumulator]
    print("error")

def runTest(l_instructions):
    l_instructions_executed = list()
    i = 0 
    accumulator = 0 
    while i not in l_instructions_executed:
        # for instruction in l_instructions:
        # print(f"instruction: {instruction.split(' ')}")
        # print(f'accumulator {accumulator}')
        l_instructions_executed.append(i)
        if i >= len(l_instructions):
            print(f"accumulator {accumulator}")
            exit(0)
        returnValue = doInstruction(l_instructions, l_instructions[i],accumulator, i)
        currentInstruction = returnValue[0]
        accumulator = returnValue[1]
        # l_changed_nop_jmp = returnValue[2]
        # houdt index bij ipv instruction
        i = currentInstruction
    # print(accumulator)
    # l_With_Bags = createBagsDict(l_infoBags)
    # recurseLookUpBag(l_With_Bags, 'shiny gold', list())

if __name__ == "__main__":
    l_instructions = getinstructions()
    
    l_changed_nop_jmp = list()
    for j in range(len(l_instructions)):
        # print(j)
        tmp_l_instruction = l_instructions.copy()
        if 'jmp' in tmp_l_instruction[j]  or 'nop' in tmp_l_instruction[j]:
            if 'jmp' in tmp_l_instruction[j]:
                tmp_l_instruction[j] = tmp_l_instruction[j].replace('jmp','nop') 
                # print(tmp_l_instruction[j])
            else: 
                tmp_l_instruction[j] = tmp_l_instruction[j].replace('nop','jmp') 
            # if out index true
            runTest(tmp_l_instruction)
        else:
            j +=1
            pass 
    
    
        


