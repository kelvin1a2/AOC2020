#!/usr/bin/python

def countLetter(letter, string):
    # print(string.count(letter))
    return string.count(letter)

def checkPassword(min, max, lettersInString):
    if lettersInString >= min and lettersInString <= max:
        return True
    return False

def readFile():
    # Using readlines() 
    file1 = open('input.txt', 'r') 
    Lines = file1.readlines() 
    
    countValidPassword = 0
    # Strips the newline character 
    for line in Lines:
        lpassword = line.split()
        min = lpassword[0].split('-')[0]
        max = lpassword[0].split('-')[1]
        lettersInString = countLetter(lpassword[1][:-1], lpassword[2])
        if checkPassword(int(min),int(max), lettersInString):
            countValidPassword += 1
    return countValidPassword


if __name__ == "__main__":
    # countLetter(letter, string)
    print("Valid passwords: " + str(readFile()))