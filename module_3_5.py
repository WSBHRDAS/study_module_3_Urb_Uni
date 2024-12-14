def get_multiplied_digits (number) :
    str_number = str(number)
    # print(str_number)
    first = int(str_number[0])

    if len(str_number) > 1:
        second = int(str_number[1:])
        if second != 0 :

            return first * get_multiplied_digits(second)
        else:
            return first
    else:
        return first

print(get_multiplied_digits(40203))
print(get_multiplied_digits(40200300))
