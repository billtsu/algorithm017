'''
Date: 2020-10-11 23:13:34
LastEditors: xub2
LastEditTime: 2020-10-11 23:17:23
FilePath: /17/242 异位词/test.py
yoo man!
'''
from typing import bool
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_set = set(s)
        t_set = set(t)
        for i in s_set:
            n_i_s = s.count(i)
            if n_i_s != t.count(i):
                return False
        return True
