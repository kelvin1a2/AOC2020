from Solution import getNumbers

def findNumber(number, l_numbers):
    # for index, item in enumerate(l_numbers):
    #     if sum(l_numbers[:(index+1)]) == number:
    if [print(f"Answer={min(l_numbers[:(index+1)]) + max(l_numbers[:(index+1)])}") for index, item in enumerate(l_numbers) if sum(l_numbers[:(index+1)]) == number]:
        return True
    return False


i = 0
while not findNumber(257342611, getNumbers()[i:]): i+=1 