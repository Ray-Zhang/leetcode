# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    if num > 6:
        return 1
    elif num < 6:
        return -1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while True:
            my_guess = (low + high) / 2
            result = guess(my_guess)
            if result > 0:
                high = my_guess - 1
            elif result < 0:
                low = my_guess + 1
            else:
                return my_guess

if __name__ == '__main__':
    s = Solution()
    print(s.guessNumber(10))
