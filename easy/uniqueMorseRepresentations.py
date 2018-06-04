alphabet = 'abcdefghijklmnopqrstuvwxyz'
morse_mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_dict = dict(zip('abcdefghijklmnopqrstuvwxyz',
            [".-","-...","-.-.","-..",".","..-.","--.","....",
                "..",".---","-.-",".-..","--","-.","---",".--.",
                "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        return len(set(map(lambda s: reduce(lambda x, y: x + y, map(lambda c: morse_dict[c], s)), words)))

if __name__ == '__main__':
    s = Solution()
    print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
