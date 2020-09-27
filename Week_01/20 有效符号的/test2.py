'''
Date: 2020-09-25 09:28:57
LastEditors: xub2
LastEditTime: 2020-09-25 09:45:29
FilePath: /xm/Users/xubiao/Documents/17/20 有效符号的/test2.py
yoo man!
'''
# -*- coding: utf-8 -*-

class Node():
    def __init__(self,val,next):
        self.val = val
        self.next = next

def run(node):
    if not (node and node.next):
        return node
    pre = node
    after = node.next
    pre.next,after.next = run(after.next),pre
    head = after
    return after
    pass

def transfer(s):
    l = s.split('-')
    lens = len(l)
    t = []
    for i in range(lens):
        node = Node(l[i],None)
        t.append(node)
    for j in range(len(t)-1):
        t[j].next = t[j+1]
    return t[0]


if __name__ == "__main__":
    i = '1-2-3-4'
    r = transfer(i)
    print(r)
    s = run(r)
    
    pass