class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for index, num in enumerate(nums):
            comp = target - num
            
            if comp in seen:
                return [seen[comp], index]
            
            else:
                seen[num] = index