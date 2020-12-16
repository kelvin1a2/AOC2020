#!/usr/bin/python
from copy import deepcopy

def getRules():
    # Using readlines() 
    f = open('Day16\input.txt', 'r')
    rules = [x.strip() for x in f.readlines()]
    d_rules = dict()
    for rule in rules:
        l_rules_numbers = list()
        if rule == '':
            break
        rule_spec = rule.split(':')[0]
        rule_numbers = rule.split(':')[1][1:].split(' or ')
        x = rule.split(':')[1][1:].split(' or ')
        for j in x:
             for i in range(list(map(int,j.split('-')))[0], list(map(int,j.split('-')))[1]+1):
                 l_rules_numbers.append(i)
        d_rules[rule_spec] = l_rules_numbers
    return d_rules

def getNearbyTickets():
    # Using readlines() 
    f = open('Day16\input.txt', 'r')
    rules = [x.strip() for x in f.readlines()]
    nearbyTickets = False
    l_nearbyTickets = list()
    for rule in rules:
        if rule == '':
            pass 
        if rule.startswith('nearby tickets:'):
            nearbyTickets = True
            continue
        if nearbyTickets:
            l_nearbyTickets.append(list(map(int,rule.split(','))))
    return l_nearbyTickets

def removeInvalidTickets(l_nearbyTickets, l_rules_numbers):
    tmp_valid_tickets = list()
    tmp_rules_numbers = list()
    for x in l_rules_numbers.values():
        tmp_rules_numbers.extend(x)
    valid = True
    for x in l_nearbyTickets:
        for xy in x:
            if xy not in tmp_rules_numbers:
                valid = False
        if valid:
            tmp_valid_tickets.append(x)
        valid = True
    return tmp_valid_tickets

def findPosition(nearbyTicket, l_rules_numbers, possibleFields):
    for indexTicket, number in enumerate(nearbyTicket): 
        # for index, number in enumerate(l_nearbyTickets):
        # print(f"test: {test}")
        for indexRules, x in enumerate(list(map(list, l_rules_numbers.values()))):
            if possibleFields[indexTicket][indexRules] == 0:
                continue 
            elif number not in x:
                # print(f"number:{number} x:{x} index:{index}")
                possibleFields[indexTicket][indexRules] = 0
    return possibleFields

if __name__ == "__main__":
    l_rules_numbers = getRules()
    l_nearbyTickets = getNearbyTickets()
    l_nearbyTickets = removeInvalidTickets(deepcopy(l_nearbyTickets), l_rules_numbers)
    # print(l_rules_numbers)
    # print(l_nearbyTickets)
    # voor 1 uit te rekenen: 
    your_ticket = [67,107,59,79,53,131,61,101,71,73,137,109,157,113,173,103,83,167,149,163]
    a_list = [1] * len(your_ticket)
    possibleFields = {i: deepcopy(a_list) for i in range(len(your_ticket))}
    for i in range(0,len(l_nearbyTickets)):
        possibleFields = findPosition(deepcopy(l_nearbyTickets[i]), l_rules_numbers, possibleFields)
    print(f"possibleFields {possibleFields}")
    tmppp =list()
    for x in possibleFields.values():
        tmppp.append(sum(x))
    tmppp.sort()
    print(tmppp)

    # possibleFields[0] = [1,1,0]
    # possibleFields[1] = [0,1,0]
    # print(f"possibleFields {possibleFields}")
    for x in l_rules_numbers.keys():
         l_rules_numbers[x] = 0
    # tmp = list()
    # # for x in tmp:
        
    # currentsum = 1
    ij = 0 
    while ij < len(possibleFields.values()):
        for index, x in enumerate(possibleFields.values()):
            for index2, y in enumerate(x):
                if sum(x) == 1 and y ==1:
                # print('asdfsd')
                    # print(x)
                    ij +=1
                    l_rules_numbers[list(l_rules_numbers)[index2]] = index
                    for idk, idk2 in enumerate(possibleFields.values()):
                        if idk2[index2] == 1:
                            idk2[index2] -= 1
                    break
                # print('asdfsd')
    tmpPost = list()
    for x in l_rules_numbers.keys():
        if x.startswith('departure'): 
            print(f"key: {x}, l_rules_numbers[key]:{l_rules_numbers[x]}")
            tmpPost.append(l_rules_numbers[x])
    answer = 1
    for row in tmpPost:
        print(f"row: {row} and your_ticket[row] {your_ticket[row]}")
        answer *= your_ticket[row]
    print(answer)

