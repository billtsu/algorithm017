'''
Date: 2020-10-12 11:09:16
LastEditors: xub2
LastEditTime: 2020-10-13 09:25:56
FilePath: /17/46 全排列/test.py
yoo man!
'''
from typing import List, Tuple

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         def backtrack(nums,tmp):
#             if not nums:
#                 res.append(tmp)
#                 return
#             for i in range(len(nums)):
#                 backtrack(nums[:i]+nums[i+1:],tmp+[nums[i]])
#         backtrack(nums,[])
#         return res

class Solution:

    def permute(self, nums: List[int])-> List[List[int]]:
        
        # def search(nums, depth, subset):
        #     if depth == len(nums):
        #         res.append(subset[:])
        #         return
        #     for i in range(len(nums)):
        #         if not flag[i]:
        #             flag[i] = True
        #             subset.append(nums[i])
        #             search(nums,depth+1,subset)
        #             flag[i] = False
        #             subset.pop()
        # res = []
        # if len(nums) == 0: return []
        # flag = [False] * len(nums)
        # search(nums,0,[])
        # return res
        def search(nums, depth, subset):
            if depth == len(nums):
                res.append(subset[:])
                return
            for i in range(len(nums)):
                if not flag[i]:
                    flag[i] = True
                    subset.append(nums[i])
                    search(nums, depth+1, subset)
                    flag[i] = False
                    subset.pop()
        res = []
        if len(nums) == 0: return []
        flag = [False] * len(nums)
        search(nums,0,[])
        return res

if __name__ == "__main__":
    s = Solution()
    res = s.permute([1,2,3])
    print(res)