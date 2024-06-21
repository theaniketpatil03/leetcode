nums = [1, 2, 3, 4, 5, 6, 8]

no_of_rotations = 3 % len(nums)
len_of_nos_to_move = len(nums) - no_of_rotations
print(len_of_nos_to_move)
new_nums = nums[:len_of_nos_to_move]
print(new_nums)
nums[0:len_of_nos_to_move] = []
print(nums)
nums.extend(new_nums)
print(nums)

