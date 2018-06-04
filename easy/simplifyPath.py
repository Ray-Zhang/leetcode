class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = []
        for p in path.split('/'):
            if p == '.' or p == '':
                continue
            elif p == '..':
                path_list = path_list[:-1]
            else:
                path_list.append(p)
        return '/' if len(path_list) == 0 else '/' + reduce(lambda a, b: a + '/' + b, path_list)
        
if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/home/"))
    print(s.simplifyPath("/a/./b/../../c/"))
    print(s.simplifyPath("/../"))
    print(s.simplifyPath("/home//foo/"))
