'''
Date: 2020-09-23 11:12:36
LastEditors: xub2
LastEditTime: 2020-09-23 14:32:20
FilePath: /d3/sums.py
yoo man!
'''
def twoSum(nums, target):
    m = 0
    for i in nums:
        res = target - i
        try:
            n = nums.index(res)
            if m!=n:
                return m,n
        except:
            pass
        finally:
            m +=1

def twoSum2(nums, target):
    kd = {nums[i]:i for i in range(len(nums))}
    m = 0
    for i in nums:
        res = target - i
        try:
            n = kd[res]
            if m != n:
                return m,n
        except:
            pass
        finally:
            m+=1

def twoSum3(nums, target):
    res = enumerate(nums)
    dic = {}
    for i ,j1 in res:
        j2 = target-j1
        if j2 in dic:
            return [dic[j2], i]
        dic[j1] = i

def twoSum4(nums, target): # 基本上是时间空间最优解
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            return i, dic[target - nums[i]]
        else:
            dic[nums[i]] = i

if __name__ == '__main__':
    t = [2,2,7,4,6]
    # res = twoSum(t,15)
    res = twoSum4(t,11)
    print(res)