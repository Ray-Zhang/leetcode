class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p, q = 0, len(nums1)-1
        r, s = 0, len(nums2)-1

    # return: tuple(median, left_end, right_start)
    def _divideByMedian(self, nums):
        if len(nums) % 2 == 0:
            return ((nums[len(nums)/2-1] + nums[len(nums)/2])/ 2.0, len(nums)/2-1, len(nums)/2)
        else:
            return (nums[len(nums)/2], len(nums)/2-1, len(nums)/2+1)

    # return: index that all elements before(exclusive/inclusive) are smaller
    def _divideByNumber(self, val, nums):
        low, high = 0, len(nums)-1
        while high - low > 0:
            idx = (high - low) / 2
            if nums[high] < val:
                return high
            if nums[low] > val:
                return low
            if nums[idx] > val:
                low = idx
            elif nums[idx] < val:
                high = idx
            else:
                return idx

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [3, 4, 5]
    print(s._divideByMedian(nums1))
    print(s._divideByMedian(nums2))
    print(s._divideByNumber(3, nums1))
    print(s._divideByNumber(3, nums2))
