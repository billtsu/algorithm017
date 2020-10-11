'''
Date: 2020-10-11 23:25:40
LastEditors: xub2
LastEditTime: 2020-10-11 23:25:50
FilePath: /17/1 两数之和/test.py
yoo man!
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            try:
                ind = nums.index(res)
            except:
                continue
            if res in nums and ind !=i:
                return i,ind