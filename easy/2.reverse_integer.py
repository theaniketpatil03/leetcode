'''
Question  - 

    Reverse the given integer

Example - 

    input - 123
    output - 321
'''

# my solution
def reverse_integer(num : int) -> int:
    reversed_int = str(num % 10)
    reminder = num // 10


    while reminder > 0:

        reversed_int += str(reminder % 10)
        reminder = reminder // 10

    return int(reversed_int)

print(reverse_integer(10002300))


# solution on website leetcode
# https://leetcode.ca/2015-12-07-7-Reverse-Integer/


def reverse(x: int) -> int:
    ans = 0
    mi, mx = -(2**31), 2**31 - 1
    while x:
        if ans < mi // 10 + 1 or ans > mx // 10:
            return 0
        y = x % 10
        if x < 0 and y > 0:
            y -= 10
        ans = ans * 10 + y
        x = (x - y) // 10
    return ans
print(reverse(10002300))