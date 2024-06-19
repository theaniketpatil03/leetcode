li = [1, 2, 3, 4, 3]

def remove_element(li, element):
    k = 0

    for x in li:
        # print(x)
        print(x, element)
        if x != element:
            print(x, element)
            # print(x)
            li[k] = x
            k += 1

    return li
def removeElement(nums, val) -> int:
    k = 0
    for x in nums:
        if x != val:
            nums[k] = x
            k += 1
    return nums
# print(remove_element(li, 3))
print(removeElement(li, 3))