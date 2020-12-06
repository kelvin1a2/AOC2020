#!/usr/bin/python

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
        self.dVotes = None 
        self.everyOneYes = 0 
        
    def printQuestions(self):
        print(f"self.L_questionsAnswers: {self.L_questionsAnswers}")
    
    def printYes(self):
        print(f"self.yes: {self.yes}")
    
    def printDuplicates(self):
        print(f"self.duplicates: {self.duplicates}")
    
    def printD_votes(self):
        print(f"self.dVotes: {self.dVotes}")
    
    def GetLengthYes(self):
        return len(self.yes)

    def calculateYes(self):
        d = dict()
        for question in self.L_questionsAnswers:
            for char in question:
                if char not in self.yes:
                    self.yes += char
                    d[char] = 1
                else:
                    self.duplicates += char
                    d[char] += 1
        self.dVotes = d 
                # print(char)

    def calculateEveryoneYes(self):
        for char in self.dVotes:
            if self.dVotes.get(char) == self.groupCount:
                self.everyOneYes +=1

    def GetEveryoneYes(self):
        return self.everyOneYes


if __name__ == "__main__":
    l_forms = getForm()
    lenAnswers = 0 
    for form in l_forms:
        # form.printQuestions()
        form.calculateYes()
        form.calculateEveryoneYes()
        lenAnswers += form.GetEveryoneYes()
        # form.printD_votes()
        # form.printYes()
        # form.printDuplicates()
    print(f"lenAnswers: {lenAnswers}")
