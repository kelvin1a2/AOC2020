#!/usr/bin/python
import math

def getForm():
    # Using readlines() 
    Forms = open("input.txt", 'r').readlines() 
    l_forms = list()
    answer = list()
    i = 0
    # form_vars = ''
    # Strips the newline character 
    for form in Forms:
        if len(Forms)-1 == i:
            answer.append(form[:-1])
            l_forms.append(Form(answer))
            break
        if form == "\n":
            # print(f"form_vars: {form_vars}")
            l_forms.append(Form(answer))
            answer = list()
        else:
            answer.append(form[:-1])
            # form_vars +=  form[:-1]
        i += 1
    return l_forms

class Form():
    def __init__(self,form_vars):
        self.groupCount = len(form_vars)
        self.L_questionsAnswers = form_vars
        self.yes = ''
        self.duplicates = '' 
        
    def printQuestions(self):
        print(f"self.L_questionsAnswers: {self.L_questionsAnswers}")
    
    def printYes(self):
        print(f"self.yes: {self.yes}")
    
    def printDuplicates(self):
        print(f"self.duplicates: {self.duplicates}")
    
    def GetLengthYes(self):
        return len(self.yes)

    def calculateYes(self):
        for question in self.L_questionsAnswers:
            for char in question:
                if char not in self.yes:
                    self.yes += char
                else:
                    self.duplicates += char
                # print(char)


if __name__ == "__main__":
    l_forms = getForm()
    lenAnswers = 0 
    for form in l_forms:
        # form.printQuestions()
        form.calculateYes()
        lenAnswers += form.GetLengthYes()
        # form.printYes()
        # form.printDuplicates()
    print(f"lenAnswers: {lenAnswers}")
