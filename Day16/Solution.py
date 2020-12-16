#!/usr/bin/python


def getRules():
    # Using readlines() 
    f = open('Day16\input.txt', 'r')
    rules = [x.strip() for x in f.readlines()]
    # d_rules = dict()
    l_rules_numbers = list()
    for rule in rules:
        if rule == '':
            break
        # rule_spec = rule.split(':')[0]
        # rule_numbers = rule.split(':')[1][1:].split(' or ')
        x = rule.split(':')[1][1:].split(' or ')
        for j in x:
            for i in range(list(map(int,j.split('-')))[0], list(map(int,j.split('-')))[1]+1):
                l_rules_numbers.append(i)
        # d_rules[rule_spec] = rule_numbers
        # print(rule_numbers)
    return list(set(l_rules_numbers))

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
            l_nearbyTickets.extend(list(map(int,rule.split(','))))
        # rule_spec = rule.split(':')[0]
        # rule_numbers = rule.split(':')[1][1:].split(' or ')
        # d_rules[rule_spec] = rule_numbers
        # l_nearbyTickets(rule_numbers)
    return l_nearbyTickets



if __name__ == "__main__":
    l_rules_numbers = getRules()
    l_nearbyTickets = getNearbyTickets()
    # print(l_rules_numbers)
    # print(l_nearbyTickets)
    answer = 0
    for number in l_nearbyTickets:
        if number not in l_rules_numbers:
            # print(number)
            answer += number
    print(f"answer {answer}")
    #     for var_range in l_rules: 
    #         # print(list(map(int,var_range.split('-')))[0])
    #         if number not in range(list(map(int,var_range.split('-')))[0], list(map(int,var_range.split('-')))[1]):
    #             print(number)
    #             break
    