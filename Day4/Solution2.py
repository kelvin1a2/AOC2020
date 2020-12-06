#!/usr/bin/python
import math
import re

def getPassports():
    # Using readlines() 
    Lines = open("input.txt", 'r').readlines() 
    L_passports = list()
    password_vars = ''
    # Strips the newline character 
    for line in Lines:
        if line == "\n":
            # print(f"pasword_vars: {password_vars}")
            L_passports.append(Passport(password_vars[1:]))
            password_vars = ''
        else:
            password_vars +=  ' ' +  line[:-1]
        # if line == Lines[-1]:
        #     print("ikkomhier")
    # print(L_passports)
    return L_passports

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def checkECL(ecl):
    if ecl == '': 
        return False
    if any(ecl in s for s in eye_colors):
        return True
    else:
        return False

class Passport():
    def __init__(self,password_vars):
        self.byr = 0
        self.iyr = 0
        self.eyr = 0
        self.hgt = ''
        self.hcl = ''
        self.ecl = ''
        self.pid = ''
        self.cid = None
        self.passport_string_from_input = password_vars
    
    def fill_key_pair_value(self, L_key_pair_values):
        key = ''
        value = ''
        for key_pair_value in L_key_pair_values:
            key = key_pair_value.split(':')[0]
            value = key_pair_value.split(':')[1] 
            if key.startswith('byr'):
                self.byr = int(value)
            elif key.startswith('iyr'):
                self.iyr = int(value)
            elif key.startswith('eyr'):
                self.eyr = int(value)
            elif key.startswith('hgt'):
                self.hgt = value
            elif key.startswith('hcl'):
                self.hcl = value
            elif key.startswith('ecl'):
                self.ecl = value
            elif key.startswith('pid'):
                self.pid = value
            elif key.startswith('cid'):
                self.cid = value        
            # print(f"key: {key}, value {value}")

    def getKeyValuePairs(self):
        return self.passport_string_from_input.split()
        # print(passport_key_value)
    
    def checkValidPassport(self):
        validity = False
        if self.byr < 1920 or self.byr > 2002:
            return validity
        if self.iyr < 2010 or self.iyr > 2020:
            return validity
        if self.eyr < 2020 or self.iyr > 2030:
            return validity
        if self.hgt[-2:] == 'cm' or self.hgt[-2:] == 'in':
            if self.hgt[-2:] == 'cm':
                if int(self.hgt[:(len(self.hgt)-2)]) < 150 or int(self.hgt[:(len(self.hgt)-2)]) > 193:
                    return validity
            if self.hgt[-2:] == 'in':
                if int(self.hgt[:(len(self.hgt)-2)]) < 59 or int(self.hgt[:(len(self.hgt)-2)]) > 76:
                    return validity
        else:
            return validity
        # if int(self.hgt[:(len(self.hgt)-2)]) < 150 or int(self.hgt[:(len(self.hgt)-2)]) > 193:
            # return validity 
        if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.hcl):
            return validity
        if not checkECL(self.ecl):
            return validity
        if not re.search(r'^(?=0+[1-9])0\d{8}$', self.pid) and not re.search(r'^\d{9}$', self.pid):
            return validity
        # if self.cid is None:
        #     return True
        return True

if __name__ == "__main__":
    L_passports = getPassports()
    validPassports = 0 
    for passport in L_passports:
        L_key_pair_values = passport.getKeyValuePairs()
        passport.fill_key_pair_value(L_key_pair_values)
        if passport.checkValidPassport():
            validPassports +=1
    print(f"Valid passports {validPassports}")

