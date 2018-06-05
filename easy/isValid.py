class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openParen = '([{'
        closeParen = ')]}'
        parenStack = []
        for p in s:
            if p in openParen:
                parenStack.append(p)
            elif p in closeParen:
                if len(parenStack) == 0:
                    return False
                last = parenStack.pop()
                if p == ')' and last == '(':
                    pass
                elif p == ']' and last == '[':
                    pass
                elif p == '}' and last == '{':
                    pass
                else:
                    return False

        if len(parenStack) > 0:
            return False
        else:
            return True

if __name__ == '__main__':
    s= Solution()
    print(s.isValid('()'))
    print(s.isValid('()[]{}'))
    print(s.isValid('{[]}'))
    print(s.isValid('([)]'))
    print(s.isValid('(]'))
    print(s.isValid('('))
    print(s.isValid(''))
