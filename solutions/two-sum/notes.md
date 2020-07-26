## Two-Sum Problem Notes

* url: https://leetcode.com/problems/two-sum

#### First Attempt

* Git tag: 'wa-01'

* My first solution was most similar to the _'Approach 1: Brute Force'_ solution on leetcode.
 * Theirs

        public int[] twoSum(int[] nums, int target) {
            for (int i = 0; i < nums.length; i++) {
                for (int j = i + 1; j < nums.length; j++) {
                    if (nums[j] == target - nums[i]) {
                        return new int[] { i, j };
                    }
                }
            }
            throw new IllegalArgumentException("No two sum solution");
        }

 * Mine
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
