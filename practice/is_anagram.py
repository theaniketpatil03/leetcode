s = 'let'
t = 'tel'

dic_1 = {}
def is_anagram(s, t):
    for char in s:
        if char in dic_1:

            dic_1[char] += 1
        else:
            dic_1[char] = 1

    for char in t:
        if char in dic_1:
            dic_1[char] -= 1
        else:
            dic_1[char] = -1
    for val in dic_1.values():
        if val != 0:
            return False

    return True

print(is_anagram(s, t))

    