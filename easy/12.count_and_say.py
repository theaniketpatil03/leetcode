'''
Question - 

The count-and-say sequence is the sequence of integers with the first five terms as following
1.     1
2.     11
3.     21
4.     1211
5.     111221
..
..
..

'''

counter = 0
char='12234444'
res = ''
def say(n):
    res = ''
    if n == 1:
        return '1'
    for i in range(len(char)):
        counter += 1
        if len(char) == i+1 or char[i] != char[i+1]:
            res += str(counter) + char[i]
            counter = 0

    return res

def say_with_num(n):
    # for i in range(n):
    #     res = '1' 
    #     counter = 0
    #     for _ in range(n - 1):
    #         counter +
    if  n==1:
        return '1'
    prev = say_with_num(n-1)
    result = ""
    count = 1

    for i in range(len(prev)):
        if i + 1 < len(prev) and prev[i] == prev[i+1]:
            count +=1
        else:
            result += str(count) + prev[i]
            count = 1

    return result

print(say_with_num(10))




        
                