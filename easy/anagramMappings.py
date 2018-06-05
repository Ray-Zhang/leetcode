class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        idx_list = []
        for ele in A:
            idx_list.append(B.index(ele))
        return idx_list

if __name__ == '__main__':
    s = Solution()
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    print(s.anagramMappings(A, B))
