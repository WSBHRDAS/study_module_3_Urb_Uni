calls = 0

def count_calls() :
    global calls
    calls += 1

def string_info (string) :
    count_calls()

    tuple_str = (len(string),string.upper(),string.lower())

    return tuple_str

def is_contains (string, list_to_search) :
    count_calls()
    string = string.upper()

    resultat = False        #нет совпадений
    for i in range(len(list_to_search)):
        if list_to_search[i-1].upper() == string :
            resultat = True
            break
    return resultat

print(string_info("Agrofoska"))
print(string_info("BraKADABRA"))
print(string_info("AgroSila"))
print(string_info("AgroEXP"))

print(is_contains('Moloko',["MoLoCHko","Mleko", "MoLoKo"]))
print(is_contains('Ahmad',["Hamad","AKHMAD","AkhmaT"]))

print (calls)