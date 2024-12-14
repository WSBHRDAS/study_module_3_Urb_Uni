def print_params(a = 1, b = 'строка', c = True) :
    print("a: ", a,"   b:", b, "  c:", c)

print_params(12, "3d", [12,2])
print_params(1.3, False, [12,2])
print_params(b = 12)
print_params(c = [1,2,5])

values_list = [777, "String"]

print_params(*values_list)

values_list.insert(0,False)
print("values_list:   ", values_list)
print_params(*values_list)

values_dict = {"a" :"1", "b" : "3", "c" :"5"}
print("values_dict:   ",values_dict)
print_params(**values_dict)

values_list_2 = [12.56, "String"]
print("values_list_2:   ",values_list_2)
print_params(*values_list_2,13.32)

