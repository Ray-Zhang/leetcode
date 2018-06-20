class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        vowels = 'aiueoAIUEO'
        front = True    # when False, search string from backward
        i, j = 0, len(s) - 1
        left, right = [], []
        vowel = None
        while i <= j:
            if front:
                if vowel:
                    left.append(vowel)
                    vowel = None
                    i += 1
                    continue
                if s[i] in vowels:
                    vowel = s[i]
                    front = False
                else:
                    left.append(s[i])
                    i += 1
            else:
                if s[j] in vowels:
                    if j > i:
                        right.append(vowel)
                    vowel = s[j]
                    front = True
                else:
                    right.append(s[j])
                j -= 1
        if vowel:
            left.append(vowel)
        right.reverse()
        return ''.join(left + right)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels("hello"))
    print(s.reverseVowels("leetcode"))
    print(s.reverseVowels("a."))
    print(s.reverseVowels("ai"))
