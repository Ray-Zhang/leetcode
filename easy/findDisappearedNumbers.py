class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = [i + 1 for i in range(n)]
        for ele in nums:
            ret[ele-1] = 0
        return filter(lambda x: x > 0, ret)

if __name__ == '__main__':
    s = Solution()
    inp = [4,3,2,7,8,2,3,1]
    print(s.findDisappearedNumbers(inp))
