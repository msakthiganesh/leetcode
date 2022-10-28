from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, val in enumerate(nums):
            req = target - val
            if req in dict:
                return dict[req], i
            dict[val] = i
            

soln_object = Solution()
print(soln_object.twoSum(nums = [2, 3, 5, 6], target = 11))
            