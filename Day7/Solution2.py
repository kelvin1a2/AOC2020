#!/usr/bin/python
import re

def getBagInfo():
    # Using readlines() 
    f = open('Day7\input.txt', 'r')
    return [x.strip() for x in f.readlines()]
    

def createBagsDict(l_infoBags):
    l_bags = list()
    a_dictionary = dict()
    for infoBag in l_infoBags:
        main_bag = infoBag[:infoBag.index(" bags contain")]
        other_bags = infoBag.split(" bags contain ")[1]
        if "no other bags." == other_bags:
            a_dictionary[main_bag] = None 
            l_bags.append(a_dictionary.copy())
            pass
        else:
            a_dictionary[main_bag] = re.findall('(\d+) (.*?) bag', other_bags)
            # print(f" a_dictionary {a_dictionary}")
            l_bags.append(a_dictionary.copy()) 
        a_dictionary = dict()
    # print(f"l_bags {l_bags}")
    return l_bags

def recurseLookUpBag(l_With_Bags, bagName, l_current_bags):
    for baginfo in l_With_Bags:
        for bag in baginfo:
            test = baginfo[bag]
            if True in [bagName in x for x in test]:
                if (len(l_current_bags) == 0 or bag not in [(list(x.keys())[0]) for x in l_current_bags]):
                # print(f"baginfo {baginfo}")
                    l_current_bags.append(baginfo)
                    # print(f"l_current_bags {l_current_bags}")
                    # print(f"l_current_bags {l_current_bags} len {len(l_current_bags)}")
                    recurseLookUpBag(l_With_Bags, bag,l_current_bags)
    return l_current_bags

globalAnswer = 0

def answerCal(answer):
    global globalAnswer 
    globalAnswer += answer
    print(globalAnswer)

def recurseLookUpBag2(l_With_Bags, bagName, l_current_bags,answer,currentIndex, currentAnswer):
    number = 0
    # answer = 0 
    # print("ikkomhier")
    i = 0 
    for baginfo in l_With_Bags:
        if bagName in [x for x in baginfo.keys()]:
            if baginfo[bagName] is None:
                return
            for item in baginfo[bagName]:
                print(f"bagname {bagName} ; item {item} ")
                # if Recursive:
                i += 1 
                number += int(item[0])
                # currentIndex = int(item[0])
                # print(f"currentIndex {currentIndex}")
                idknow = currentIndex * int(item[0]) 
                # if bagName == 'shiny gold' and idknow:
                # print(f"idknow {idknow}")
                # print(f"answer {answer}")
                if bagName == 'shiny gold':
                    answer = 0
                    i = 0
                # else:
                answer += idknow
                # print(f"idknow {idknow}")
                if (len(baginfo[bagName]) == i) and bagName != 'shiny gold': 
                    # if len(baginfo[bagName]) != 1:
                     for Z in [x for x in l_With_Bags]:
                        if item[1] in Z:
                            if Z[item[1]] is None:
                                # print('hoit')
                                print(f"answer {answer}")
                                answerCal(answer)
                biem = recurseLookUpBag2(l_With_Bags, item[1], l_current_bags,answer, (currentIndex * int(item[0])), currentAnswer)
                # print(f"biem {biem}")
                # print(f"answer {answer}")
                # answer = 0
                # currentIndex = 1
                # if biem != 0:
                    # answer += biem * int(item[0]) + int(item[0])
                    # print(answer)
                # print(f"item: {int(item[0])}")
            # print(f"numberna: {numberna}")
        # print(f"numbernaxx: {number}")    
    # print(f"numbernaxx2: {number}") 
    # print(answer)
    return number

if __name__ == "__main__":
    l_infoBags= getBagInfo()
    l_With_Bags = createBagsDict(l_infoBags)
    test = recurseLookUpBag2(l_With_Bags, 'shiny gold', list(), 0, 1, 0)
    # for x in test:
    #     print(x)
        


