#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([1 for x in S if x in J])

if __name__ == '__main__':
    s = Solution()
    J = "aA"
    S = "aAAbbbb"
    print(s.numJewelsInStones(J, S))
