'''
Question

Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

'''

li = [1,3,5,6]
val = 3


def search_or_insert_position(nums, val):
    post = 0

    for x in nums:
        if x < val:
            post += 1
        # else:

    if post > len(nums):
        nums.append(val)
    else:
        if nums[post] != val:
            nums.insert(post, val)

    return nums, post

print(search_or_insert_position(li, val))

# website solution

def searchInsert(nums, target) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left