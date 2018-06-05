class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u_cnt, d_cnt, l_cnt, r_cnt = 0, 0, 0, 0
        for m in moves:
            if m == 'U':
                u_cnt += 1
            elif m == 'D':
                d_cnt += 1
            elif m == 'L':
                l_cnt += 1
            else:
                r_cnt += 1
        return u_cnt == d_cnt and l_cnt == r_cnt

if __name__ == '__main__':
    s = Solution()
    print(s.judgeCircle("UD"))
    print(s.judgeCircle("LL"))
