class Solution:

    def factorTarget(self, nums, target):
        #target = x1 + x2
        #x2 = target - x1
        num_val = {}
        for i, num in enumerate(nums):
            num_val[num]=i
        for num in nums:
            ##Find factors
            ##Check hashtable for factors
            ##Return index (numval_[num]) of item using hash table

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        factors = self.factorTarget(nums, target)
        if factors is not None:
            return factors
        return None
