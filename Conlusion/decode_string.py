# coding: utf-8

class Solution(object):
    def __init__(self):
        self._idx = 0

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        queue = list()
        queue.append(['', 1])
        num = ""

        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                queue.append(['', int(num)])
                num = ""
            elif c == ']':
                st, k = queue.pop()
                queue[-1][0] += k * st
            else:
                queue[-1][0] += c

        return queue[0][0]

    def recusive(self, s):
        self._idx = 0
        return self._recusive(s)

    def _recusive(self, s):
        num = 0
        word = ""
        while self._idx < len(s):
            cur = s[self._idx]
            if cur == '[':
                self._idx = self._idx + 1
                curStr = self._recusive(s)
                word += curStr*num
                num  = 0
            elif cur.isdigit():
                cur_num = 10 * num  + int(cur)
                num = cur_num + num
            elif cur == ']':
                return word
            else:
                word += cur
            self._idx += 1
        return word


if __name__ == '__main__':
    solution = Solution()
    # assert solution.decodeString("3[a]2[bc]") ==  "aaabcbc"
    # assert solution.decodeString("3[a2[c]]") ==  "accaccacc"
    # assert solution.decodeString("2[abc]3[cd]ef") ==  "abcabccdcdcdef"
    
    assert solution.recusive("3[a]2[bc]") ==  "aaabcbc"
    assert solution.recusive("3[a2[c]]") ==  "accaccacc"
    assert solution.recusive("2[abc]3[cd]ef") ==  "abcabccdcdcdef"


