# O(n) solution for the "Two Sum" problem using a Hash Map

# To run locally, uncomment lines 5 and lines 37-48

# from typing import List

# Logic wrapper to satisfy LeetCode formatting requirements
class Solution:

	"""
	Define the function as `twoSum`
	Argument `self` for class instance
	Type-hinted variable `nums` implies a list of integers
	Type-hinted variable `target` implies an integer
	Type hint for return value as a list of integers (index positions) 
	"""
	def twoSum(self, nums: List[int], target: int) -> List[int]:

		# Dictionary to store map of `{number: index}`
		num_map = {}

		# Loop through list using index `i` and value `num`
		for i, num in enumerate(nums):

			# Compute the complement `c`
			c = target - num

			# Check `num_map` for `c`
			if c in num_map:

				# Return indices of a complementary set
				return [num_map[c], i]
			
			# If complement not found, store current number's index
			num_map[num] = i

"""
in_nums = [2, 7, 11, 15]
in_targ = 9

indices = Solution.twoSum(0, in_nums, in_targ)

pos1 = indices[0]
pos2 = indices[1]

print(f"Index = {indices}")
print(f"Value = [{in_nums[pos1]}, {in_nums[pos2]}]")
"""
