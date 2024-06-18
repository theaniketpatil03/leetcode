'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''
from itertools import pairwise
# from 

roman_letters = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
def roman_to_int(roman: str) -> int:
    # print(list(pairwise(roman)))
    value = 0
    for a , b in pairwise(roman):
        # print(roman_letters[a], b)
        print(a, b)
        if roman_letters[a] < roman_letters[b]:
            print(a, roman_letters[a] * -1)
            value += (roman_letters[a] * -1)
        else:  
            print(a, roman_letters[a] * 1)
            value += roman_letters[a] 

    value += roman_letters[roman[-1]]

    return sum( (-1 if roman_letters[a] < roman_letters[b] else 1) * roman_letters[a] for a , b in pairwise(roman)) + roman_letters[roman[-1]]

    print(sum)

    

print(roman_to_int('MCMXCIV'))
# pairwise('III')