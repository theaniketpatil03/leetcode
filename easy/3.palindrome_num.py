'''
Question - 
    Determine whether an integer is a palindrome.
    An integer is a palindrome when it reads the same backward as forward.
'''


# my solution
def reverse_integer(num : int) -> int:
    reversed_int = str(num % 10)
    reminder = num // 10

    # print(reversed_int)
    if num == 0 :
        return 'zero not accepted'
    elif int(reversed_int) == 0:
        return 'it is not palindrom'
    while reminder > 0:

        reversed_int += str(reminder % 10)
        reminder = reminder // 10
    print(reversed_int)
    if num == int(reversed_int):
        return 'it is palindrome'
    return 'it is not palindrome'
print(reverse_integer(10))

# another approch
# https://leetcode.ca/2015-12-09-9-Palindrome-Number/