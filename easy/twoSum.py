class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def unittest(self):
        nums = [2, 7, 11, 15]
        target = 9
        print(self.twoSum(nums, target))

if __name__ == '__main__':
    sol = Solution()
    sol.unittest()

