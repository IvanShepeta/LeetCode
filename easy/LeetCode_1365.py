#TODO Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # r = []
        # count = 0
        # for num in nums:
        #     for other in nums:
        #         if num > other:
        #             count += 1
        #     r.append(count)
        #     count = 0
        # return r
        r = sorted(nums)
        di = {}
        for i, j in enumerate(r):
            if j not in di:
                di[j] = i
        res = []
        for i in nums:
            res.append(di[i])
        return res

s = Solution()
nums = [8,1,2,2,3]
result = s.smallerNumbersThanCurrent(nums)
print(result)