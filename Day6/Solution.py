#!/usr/bin/python

def getForm():
    # Using readlines() 
    f = open('Day6\input.txt', 'r')
    Forms = [x.strip() for x in f.readlines()]
    l_forms = list()
    answer = list()
    for form in Forms:
        if form != '':
            answer.append(form)
        else:
            l_forms.append(Form(answer))
            answer = list()
    l_forms.append(Form(answer))
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
