#!/usr/bin/python

def retrieveLetterFromPostion(string, letter, positions):
    min = positions.split('-')[0] # 1
    max = positions.split('-')[1] # 3
    count = 0 
    # print(string)
    if string[int(min)-1] == letter:
        count +=1
    if string[int(max)-1] == letter:
        count +=1
    if count == 1:
        return True
    return False

def readFile():
    # Using readlines() 
    file1 = open('input.txt', 'r') 
    Lines = file1.readlines() 
    
    countValidPassword = 0
    # Strips the newline character 
    for line in Lines:
        lpassword = line.split() # 1-3 a: abcde
        if retrieveLetterFromPostion(lpassword[2], lpassword[1][:-1], lpassword[0]):
            countValidPassword += 1
    return countValidPassword


if __name__ == "__main__":
    # countLetter(letter, string)
    print("Valid passwords: " + str(readFile()))
    #list with passwords