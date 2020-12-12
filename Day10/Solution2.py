#!/usr/bin/python
import re

def getJoltest():
    return [int(x) for x in open('Day10/input.txt').read().splitlines()]

def checkList(l_joltes, count, lastItem):
    count += 1 
    for index , item in enumerate(l_joltes):
        i = 0 
        diff = 0 
        while diff <= 3:
            i+=1
            if l_joltes[-i] == l_joltes[index] or l_joltes[-1] == l_joltes[index+i]:
                break
            else: 
                diff = l_joltes[index+i] - l_joltes[index]
                if diff == 3:
                    if i == 1:
                        break
                    l_tmp = l_joltes.copy()
                    if i == 3:
                        l_tmp.pop(index+1)
                        l_tmp.pop(index+1)
                    elif i == 2: 
                        l_tmp.pop(index+1)
                    x = l_tmp.index(item)
                    count = checkList(l_tmp[x:], count,item)    
                elif diff == 2:
                    if i == 1:
                        break
                    l_tmp = l_joltes.copy()
                    l_tmp.pop(index+1)
                    x = l_tmp.index(item)
                    count = checkList(l_tmp[x+1:], count,item)
                elif diff == 1:
                    pass
                else:
                    pass
    #grep a coffee or two xd 
    print(f"count {count}")
    return count 

if __name__ == "__main__":
    l_joltes = getJoltest()
    l_joltes.sort()
    l_joltes.append(l_joltes[-1] + 3)
    l_joltes.insert(0,0)
    print(l_joltes)
    checkList(l_joltes, 0, 0)