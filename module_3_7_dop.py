from ipaddress import summarize_address_range

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def is_dict (element): # проверка на содержание именованной последовательности
    return isinstance(element, dict)

def is_list (element): # проверка на содержание последовательности
    return any([isinstance(element, list), isinstance(element, tuple), isinstance(element, set)])

print ("Сумма всех чисел и длин строк Структуры data_structure:")

summ = 0

def calculate_structure_sum(data_structure) :
    global summ

    for i in data_structure:
        if is_dict(i) == True:
             for idict in i :
                 # print ("value:", i[idict])
                 if isinstance(i[idict], str) == True:
                    summ += len(i)
                 elif isinstance(i[idict], int) == True:  # подразумевается что остаются только числа
                    summ += i[idict]
                 else:
                    calculate_structure_sum(i[idict])
                 summ += len(idict)

        elif is_list(i) == True:
            calculate_structure_sum(i)

            # print("List or Tuple or Set: ")
        elif isinstance(i,str) == True:
            summ += len(i)
        else :                    #подразумевается что остаются только числа
            summ += i
        # print (i)
    return summ

result = calculate_structure_sum(data_structure)
print(result)
