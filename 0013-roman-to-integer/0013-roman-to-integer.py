class Solution:
    def romanToInt(self, s: str) -> int:
        roman = ["I", "V", "X", "L", "C", "D", "M"]
        values = [1, 5, 10, 50, 100, 500, 1000]
        roman_map = {}

        
        for i in range(len(roman)):
            roman_map[roman[i]] = values[i]

        total = 0

        
        for i in range(len(s)):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]

        return total