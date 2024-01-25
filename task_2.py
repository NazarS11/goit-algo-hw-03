import random

def get_numbers_ticket(min, max, quantity):
    list = []
# input validation, if at least 1 statement = True return empty list
    if min < 1 or max > 1000 or quantity > max:
        print (list)
        return list
    else:
        while len(list) < quantity:
            a = random.randint(min,max)
# uniqueness check
            if a not in list:
# add unique random int number in the list
                list.append(random.randint(min,max))
# sort list
        list.sort()
        print(list)
        return list

get_numbers_ticket(0,50,6)