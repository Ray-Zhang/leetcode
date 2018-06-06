class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        takeover = False
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] < 9:
                digits[idx] += 1
                takeover = False
                break
            else:
                digits[idx] = 0
                takeover = True
        if takeover:
            digits[0:0] = [1]
        return digits

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,2,3]))
    print(s.plusOne([4,3,2,1]))
    print(s.plusOne([9,9,9,9]))
    print(s.plusOne([8,9,9,9]))
