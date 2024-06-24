nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]


class Solution:
    def merge(self, nums1, nums2):
        k = len(nums1) - 1
        i = len(nums1) - len(nums2) - 1
        j = len(nums2) - 1


        while j >= 0:
            if i >=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -=1
            else:
                nums1[k] = nums2[j]
                j -=1

            k -=1



        return nums1
    

sol = Solution().merge(nums1, nums2)

print(sol)