strings = ['flower', 'flow', 'flaw']


# make first string as base
# iterate for index of base of len of base
# inside it iterate for remaining string from array
# check if len of string == index of base or string of index of base not equl to string of base of index return base till indx of base
# inside it check if index of base is equal 0 


def find_com_pre():
    prefix = ''

    base = strings[0]

    for index_of_base in range(len(base)):
        for string in strings[1:]:

            if len(string) == index_of_base or string[index_of_base] != strings[0][index_of_base]:
                if index_of_base == 0:
                    return 'no matching'
                return base[:index_of_base]
    return base

print(find_com_pre())

    

def find_com(vals):
    base = vals[0]

    for index_of_base in range(len(base)):
        for string in vals[1:]:
            if len(string) == index_of_base or string[index_of_base] != base[index_of_base]:
                if index_of_base == 0:
                    return 'no common prefix'
                return base[:index_of_base]

    return base

print(find_com(strings)) 