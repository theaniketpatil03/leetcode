

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

class Solution:
    def merge(self, nums1, m, nums2, n):

        i = m - 1 # 3 - 1 = 2
        j = n - 1 # 3 - 1 = 2
        k = m + n - 1 # 3 + 3 - 1 = 5


        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1

sol = Solution().merge(nums1, m, nums2,n)

print(sol)
