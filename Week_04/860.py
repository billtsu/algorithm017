'''
Date: 2020-10-15 13:20:35
LastEditors: xub2
LastEditTime: 2020-10-15 23:40:21
FilePath: /17/860 lemonwater/test.py
yoo man!
'''
# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

# 顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

# 注意，一开始你手头没有任何零钱。

# 如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

# 示例 1：

# 输入：[5,5,5,10,20]
# 输出：true
# 解释：
# 前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
# 第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
# 第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
# 由于所有客户都得到了正确的找零，所以我们输出 true。
# 示例 2：

# 输入：[5,5,10]
# 输出：true
# 示例 3：

# 输入：[10,10]
# 输出：false
# 示例 4：

# 输入：[5,5,10,10,20]
# 输出：false
# 解释：
# 前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
# 对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
# 对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
# 由于不是每位顾客都得到了正确的找零，所以答案是 false。
 

# 提示：

# 0 <= bills.length <= 10000
# bills[i] 不是 5 就是 10 或是 20
import copy
from types import CodeType
class Solution:
    # [5,5,10,10,20]
    def play2(self,payments,res):
        for i in range(len(payments)):
            m = payments[i]
            # 大于5 且res 长度为0
            if m > 5 and len(res) ==0: return False
            # res 长度大于0
            if len(res) >0 and m == 10:
                if res.count(5)>0: 
                    res.append(m)
                    res.remove(5)
                    return True
                return False
            if len(res) >0 and m == 20:
                if res.count(5) >=3: 
                    res.append(20)
                    res.remove(5)
                    res.remove(5)
                    res.remove(5)
                    return True
                if res.count(5) >=1 and res.count(10)>=1: 
                    res.append(20)
                    res.remove(10)
                    res.remove(5)
                    return True
                return False
            if m == 5: res.append(5)
    def play3(self,payments,res):
        for i in range(len(payments)):
            m = payments[i]
            if m == 5: res['5'] +=1
            if m == 10:
                res['10'] +=1
                res['5'] -=1
                if res['5'] <0:return False
            if m == 20:
                if res['5']<3 and res['10']<1:
                    return False
        return True
    def play(self, payments):
        res = {'5':0,'10':0,'20':0}
        for i in range(len(payments)):
            m = payments[i]
            if m == 5: res['5'] +=1
            if m == 10:
                res['10'] +=1
                res['5'] -=1
                if res['5'] <0:return False
            if m == 20:
                if res['5']>1 and res['10']>1:
                    res['10'] -=1
                    res['5'] -=1
                    res['20'] +=1
                    continue
                if res['10']<1 and res['5']<3:
                    res['5'] -=3
                    res['20'] +=1
                    continue
                return False
        return True

            


        
        pass

if __name__ == "__main__":
    s = Solution()
    p = [5,5,10,10,20]
    # p = [10,10]
    # p = [5,5,10]
    p = [5,5,5,10,5,5,10,20,20,20]
    res = []
    res = {'5':0,'10':0,'20':0}
    result = s.play(p)
    print(result)