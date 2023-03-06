# Leetcode: 1 - Two Sum

'''
Solution Logic:

For each number in the array, check to see if it
and any other number in the array besides itself
equal to the target.
'''

def twoSum(nums: list[int], target: int) -> list[int]:
	for i in range(len(nums)):
		for j in range(len(nums)):
			if i == j:
				continue
			if nums[i] + nums[j] == target:
				return [i, j]


if __name__ == '__main__':
	assert twoSum([2,7,11,15], 9) == [0, 1]
	print("Test Case 1 Passed")
	assert twoSum([3,2,4], 6) == [1, 2]
	print("Test Case 2 Passed")
	assert twoSum([3,3], 6) == [0, 1]
	print("Test Case 3 Passed")