class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for index, num in enumerate(nums):
            comp = target - num

            for index_slice, num in enumerate(nums[index+1:]):
                if comp == num:
                    index_match = index + 1 + index_slice

                    return [index, index_match]