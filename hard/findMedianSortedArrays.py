class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        # divide both lists by median of the longer list
        if len1 >= len2:
            median, lesser1, greater1 = _divideByMedian(nums1)
            lesser2, greater2 = _divideByNumber(median, nums2)
        else:
            median, lesser2, greater2 = _divideByMedian(nums2)
            lesser1, greater1 = _divideByNumber(median, nums1)

    # return: tuple(median, left_list, right_list)
    def _divideByMedian(self, nums):
        if len(nums) % 2 == 0:
            return ((nums[len(nums)/2-1] + nums[len(nums)/2])/ 2.0, nums[:len(nums)/2], nums[len(nums)/2:])
        else:
            return (nums[len(nums)/2], nums[:len(nums)/2], nums[len(nums)/2+1:])

    def _divideByNumber(self, val, nums):
        low, high = 0, len(nums)
        idx = len(nums) / 2
        while high - low > 1:
            idx = len(nums) / 2
            if val >= nums[idx-1] and val <= nums[idx]:
                return (nums[:idx], nums[idx:])
            elif val < nums[idx-1]:
                high = idx - 1
            else:
                low = idx + 1
        return (nums[:high], nums[high:])

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [3, 4, 5]
    #print(s._divideByMedian(nums1))
    #print(s._divideByMedian(nums2))
