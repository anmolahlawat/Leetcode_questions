class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        ch = ""

        for ch in s:
            dict[ch] = dict.get(ch , 0) +1

        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1
