nums = [3,2,2,3]
val = 3


class Solution:
    def removeElement(self, nums, val):
        # k = 0
        # for index in range(len(nums)):
        #     print(index)
        #     if nums[k] == val:
        #         del nums[k]
        #     else:
        #         k+=1
        # print(nums)
        # return k

        k = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[k] = nums[index]

                k += 1

        return k



sol = Solution().removeElement(nums, val)

print(sol)


