
nums = [3, 1, 2, 3, 4, 4, 5]

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # for index, num in enumerate(nums) :
    #     if num in nums[index+1:]:
    #         return num

    res = []

    for n in nums:
        n = abs(n)
        # print(n)
        print(nums[n-1])
        if nums[n-1] < 0:
            res.append(n)
        nums[n-1] = -nums[n-1]  
            

    return res

print(findDuplicate(nums))