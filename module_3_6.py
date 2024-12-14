from types import new_class


def find_max(list_r) :
    max_i = list_r[0]
    for i in list_r:
        if i > max_i :
            max_i = i
    return max_i

print(find_max([23,4,5657,8,908,808,98887]))

def count_even(list_r):
    counter = 0
    for i in list_r:
        if i == 0 :
            continue
        if i % 2 == 0:
            counter += i
    return counter

print(count_even([23,4,5657,8,98,2,98887]))

def unique(list_r) :
    new_list = {}
    new_list = set(list_r)
    list(new_list)
    # for i in list_r :
    #     if i not in new_list:
    #         new_list.append(i)

    return new_list

print(unique([23,45,5657,8,98,2,98887,23,4,5657,8,98,2,98,2,8887]))
