'''
Date: 2020-09-24 10:25:35
LastEditors: xub2
LastEditTime: 2020-09-24 11:13:40
FilePath: /ehr0/Users/xubiao/Documents/17/189 旋转数组/test.py
yoo man!
'''
# -*- coding: utf-8 -*-
'''
旋转数组
[1,2,3,4,5,6,7] k =3 [5,6,7,1,2,3,4]
[1,2,3,4,5,6,7] k=1 [7,1,2,3,4,5,6]
[1,2,3,4,5,6,7] k=2 [6,7,1,2,3,4,5]
原地替换
三种解法 空间复杂度为o(1)
[1,2,3,4,5,6,7] k =3 [5,6,7,1,2,3,4]

递归找最近解法
nums = rotate(route(nums,k-1),1)
尾部出，头部进
pop insert(0,xx)
第三种解法 三次翻转
[1,2,3,4,5,6,7]=>[4,3,2,1,5,6,7]=>[4,3,2,1,7,6,5]=>[5,6,7,1,2,3,4]

'''
def rotate(nums,k):
    if k ==1:
        lens = len(nums)
        for i in range(lens-1):
            nums[i], nums[lens-1] = nums[lens-1], nums[i]
    else:
        rotate(rotate(nums,k-1),1)
    return nums

def rotate2(nums,k):
    tmp = None
    for i in range(k):
        tmp = nums.pop()
        nums.insert(0,tmp)
    return nums
    
def rotate3(nums,k):
    lens = len(nums)
    p1 = nums[:lens-k]
    p2 = nums[lens-k:]
    p1.reverse()
    p2.reverse()
    p1.extend(p2)
    p1.reverse()
    return p1

    pass
        
if __name__ == '__main__':
    t = [1,2,3,4,5,6,7]
    # t=[1,2,3]
    k =3
    res = rotate3(t,k)
    print(res)

    pass
