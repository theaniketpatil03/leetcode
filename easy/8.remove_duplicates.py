l1 = [1, 1, 2, 3, 3, 4, 4, 4, 5]

def remove_duplicates(nums):

    k = 0

    for x in l1:
        if k ==0 or x !=nums[k-1]:
            nums[k] = x

            k += 1
    return nums

print(remove_duplicates(l1))