# -*- coding: utf-8 -*-
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.tmp = []


    def push(self, x: int) -> None:
        self.tmp.append(x)


    def pop(self) -> None:
        self.tmp.pop()


    def top(self) -> int:
        return self.tmp[-1]


    def getMin(self) -> int:
        min = self.tmp[0]
        for i in self.tmp:
            if i < min:
                min = i
        return min