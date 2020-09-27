'''
Date: 2020-09-24 10:10:43
LastEditors: xub2
LastEditTime: 2020-09-24 10:23:47
FilePath: /ehr0/Users/xubiao/Documents/17/d4/test.py
yoo man!
'''
#-*- coding:utf-8 -*-
'''
删除排序数组中的重复项
# 排序数组
# 原地删除重复项
# 返回移除后数组的长度
# 使用O(1)额外空间
'''

def rm_dup(nums):
    tmp = None
    length = len(nums)
    i = 0
    while (i<length):
        if nums[i] != tmp:
            tmp = nums[i]
            i +=1
        else:
            nums.remove(nums[i])
            length -= 1
    return nums
    pass

if __name__ == "__main__":
    t = [0,0,1,1,2,2,3,3,4,4]
    res = rm_dup(t)
    print(res)