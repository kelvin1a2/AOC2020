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
            # a_dictionary[main_bag] = None 
            # l_bags.append(a_dictionary.copy())
            pass
        else:
            a_dictionary[main_bag] = re.findall('\d (.*?) bag', other_bags)
            # print(f" a_dictionary {a_dictionary}")
            l_bags.append(a_dictionary.copy()) 
        a_dictionary = dict()
    # print(f"l_bags {l_bags}")
    return l_bags

def recurseLookUpBag(l_With_Bags, bagName, l_current_bags):
    for baginfo in l_With_Bags:
        for bag in baginfo:
            test = baginfo[bag]
            if bagName in test:
                if (len(l_current_bags) == 0 or bag not in [(list(x.keys())[0]) for x in l_current_bags]):
                # print(f"baginfo {baginfo}")
                    l_current_bags.append(baginfo)
                    # print(f"l_current_bags {l_current_bags}")
                    print(f"l_current_bags {l_current_bags} len {len(l_current_bags)}")
                    recurseLookUpBag(l_With_Bags, bag,l_current_bags)
    return l_current_bags

if __name__ == "__main__":
    l_infoBags= getBagInfo()
    l_With_Bags = createBagsDict(l_infoBags)
    recurseLookUpBag(l_With_Bags, 'shiny gold', list())
        


