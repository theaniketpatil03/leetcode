array = [0, 0, 1, 1, 1, 2, 3 ,4, 4]
print(array)

count = 1
for index in range(1, len(array)):
    # print(index, val)
    if array[index] != array[index -1]:
        array[count] = array[index]
        count+=1
print(count)

print(array)