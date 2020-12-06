#!/usr/bin/python
import math

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

class Passport():
    def __init__(self,password_vars):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None
        self.passport_string_from_input = password_vars
    
    def fill_key_pair_value(self, L_key_pair_values):
        key = ''
        value = ''
        for key_pair_value in L_key_pair_values:
            key = key_pair_value.split(':')[0]
            value = key_pair_value.split(':')[1] 
            if key.startswith('byr'):
                self.byr = value
            elif key.startswith('iyr'):
                self.iyr = value
            elif key.startswith('eyr'):
                self.eyr = value
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
        valid = False
        if self.byr is None:
            return valid
        if self.iyr is None:
            return valid
        if self.eyr is None:
            return valid
        if self.hgt is None:
            return valid
        if self.hcl is None:
            return valid
        if self.ecl is None:
            return valid
        if self.pid is None:
            return valid
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

