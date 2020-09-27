'''
Date: 2020-09-27 10:14:19
LastEditors: xub2
LastEditTime: 2020-09-27 10:30:34
FilePath: /299 bullcow/test2.py
yoo man!
'''
# -*- coding: utf-8 -*-

def main(s,g):
    s = list(s)
    g = list(g)
    S = []
    G = []
    a = 0
    b = 0
    for i, v in enumerate(g):
        if v == s[i]:
            S.append(v)
            a+=1
        else:
            G.append(v)
            S.append(s[i])
    for j in list(set(S)):
        if j in G:
            b +=1
    return str(a)+'A'+str(b)+'B'

            
    pass


if __name__ == "__main__":
    # secret = "1123"
    # guess = "0111"
    secret = "1807"
    guess = "7810"
    res = main(secret,guess)
    print(res)
    pass