class Solution:

    def factorTarget(self, nums, target):
        for i, n1 in enumerate(nums, start=0):
            for j, n2 in enumerate(nums, start=i+1):
                if j < len(nums):
                    if n1+nums[j] == target:
                        return i, j

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        factors = self.factorTarget(nums, target)
        if factors is not None:
            return factors
        return None
