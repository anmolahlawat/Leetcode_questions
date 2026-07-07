class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = {}
        for ch in s:
            if ch in x:
                x[ch] +=1
            else:
                x[ch] = 1

        for ch in t:
            if ch not in x:
                return False
            else:
                x[ch] -=1

        if all(value == 0 for value in x.values()):
            return True
        else:
            return False