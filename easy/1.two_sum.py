'''
Question - 

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example-

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

li = [1, 3, 5, 6, 8, 11, 2]
tup = (3, 1)
# print(sorted(tup))
# copy_list = li.copy()
# copy_list.pop(1)
# print(li)
# print(copy_list)
# print(li.index(11))


def check_target_sums(input_list, target):
    print(input_list)
    print(target)
    index_of_adder = []
    for i in range(len(input_list)):
        print('index', i)
        print('main lilst', li)
        adding_list = li.copy()
        adding_list.pop(i)
        print(adding_list)
        for item in adding_list:
            if input_list[i] + item == target:
                if sorted((i,input_list.index(item))) not in index_of_adder:

                    index_of_adder.append(sorted((i,input_list.index(item))))
    return index_of_adder

# output = check_target_sums(li, 9)
# print(output)

li = [1, 3, 5, 6, 8, 11, 2]
def sum_finder(nums, target):
    dic = {}
    for index, value in enumerate(nums):
        second_value = target - value
        if second_value in dic:
            return [dic[second_value], index]
        dic[value] = index

class Solution:
    def twoSum(self, nums, target) -> list:
        m = {}
        for i, x in enumerate(nums):
            y = target - x
            print(x)
            print(m)
            if y in m:
                return [m[y], i]
            m[x] = i


sol = Solution()
print(sol.twoSum(li, 9))


def trying_by_my_self(input_list, target):
    hash_table = {}

    for index, value in enumerate(input_list):
        second_value = target - value

        if second_value in hash_table:
            return [hash_table[second_value], index]

        hash_table[value] = index

print(trying_by_my_self(li, 7))
