'''
Date: 2020-09-24 11:23:59
LastEditors: xub2
LastEditTime: 2020-09-26 00:06:39
FilePath: /21 两个有序链表合并/test.py
yoo man!
'''
# —*- coding:utf-8 -*-
'''
1->2->3 1->4->6
1->1->2->3->4->6
'''
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return('{}->{}'.format(self.value,self.next))

def recurse_value(node):
    tmp = [node.value]
    if node.next:
        ret = recurse_value(node.next)
        tmp.extend(ret)
    return tmp

def form_link(nums):
    tmp = []
    for i in range(len(nums)):
        tmp.append(Node(nums[i]))
    for j in range(len(nums)):
        try:
            tmp[j].next = tmp[j+1]
        except:
            # tmp[j].next = None
            pass
    return tmp[0]

def join(node1,node2):
    tmp = recurse_value(node1)
    tmp2 = recurse_value(node2)
    print(tmp,tmp2)
    tmp.extend(tmp2)
    res = sorted(tmp)
    print('res:',res)
    ret = form_link(res)
    print('ret,',ret)
    return ret

def join2(l1,l2):
    t=[]
    def get(n):
        t.append(n)
        if n.next:
            get(n.next)
    get(l1)
    get(l2)
    return t[0]

def join3(l1,l2):
    dic = {}
    def get(n):
        if dic.get(n.value):
            dic[n.value].append(n)
        else:
            dic[n.value] = [n]
        if n.next:
            get(n.next)
    get(l1)
    get(l2)
    keys = sorted(dic.keys())
    t= []
    for k in keys:
        t.extend(dic[k])
    for i in range(len(t)-1):
        t[i].next = t[i+1]
    return t[0]
        
def join4(l1,l2):
    dic = {}
    def run(n):
        pre = n
        while pre.next:
            
            if dic.get(pre.value):
                pre.next = dic.get(pre.value)
            else:
                pre.next = None
            dic[pre.value] = pre
            pre = pre.next
            
    run(l1)
    print('dic1:',dic)
    run(l2)
    print('dic:',dic)
    sortedlist = set(dic.keys())
    def add(n1,n2):
        t = n1
        if t.next:
            add(t.next,n2)
        else:
            return t
    fnode = dic[list(sortedlist)[0]]
    for i in range(len(sortedlist)-1):
        n1 = dic[list(sortedlist)[i]]
        n2 = dic[list(sortedlist)[i+1]]
        add(n1,n2)
    return fnode

    pass

def join5(l1,l2):
    if not l1: return l2
    if not l2: return l1
    if l1.value <= l2.value:
        l1.next = join5(l1.next,l2)
        return l1
    if l1.value == l2.value:
        l2.next = join5(l1,l2.next)
        return l2
    
if __name__ == '__main__':
    n1 = form_link([1,2,3])
    n2 = form_link([1,4,6])
    print(n1,n2)
    ret= join5(n1, n2)
    print(ret)
    tl = recurse_value(ret)
    print(tl)
    pass