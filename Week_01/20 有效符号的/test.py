'''
Date: 2020-09-24 21:39:24
LastEditors: xub2
LastEditTime: 2020-09-24 23:19:31
FilePath: /xm/Users/xubiao/Documents/17/20 有效符号的/test.py
yoo man!
'''
# -*- coding: utf-8 -*-
import copy

class Stack():
    def __init__(self):
        self.tmp = []
        pass

    def push(self,item):
        self.tmp.append(item)

    def pop(self,t):
        self.tmp = self.tmp[:t]


    def flush(self):
        t = copy.copy(self.tmp)
        self.tmp = []
        return t

    def __len__(self):
        return len(self.tmp)
        
    def __repr__(self):
        return ''.join(self.tmp)
        # return 'hehe'

    def last(self):
        return self.tmp[-1]

def test(s):
    dic = {'{':'}', '(':')', '[':']'}
    if len(s)%2 != 0: return False
    for k,v in dic.items():
        if s.count(k) != s.count(v): return False
    stk = Stack()
    t = 0
    for i in range(len(s)):
        stk.push(s[i])
        # try:
        if s[i] == dic[s[t]] and i >0:
            print('res1:',stk.tmp)
            res = stk.tmp[t:]
            stk.pop(t)
            print('res:',res)
            if len(res) >2:
                return False
            if t>0:
                t -=1
            else:
                t = 0
        else:
            t+=1
            # except:
            #     return False
    
    return True
        
if __name__ == '__main__':
    ts = "()"
    ts = "()[]{}"
    # ts = "([]())[]"
    # ts = "({[)"
    # ts = "{[]}"

    print(test(ts))
    pass