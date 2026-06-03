class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }  

        subtracted = {
            'I': ('V','X'),
            'X': ('L','C'),
            'C': ('D','M')
        }
        val = 0
        for i in range(len(s)):
            if s[i] in subtracted.keys() and i<len(s)-1:
                if s[i+1] in subtracted[s[i]]:
                    val -= romanNum[s[i]]
                    continue
            val+= romanNum[s[i]]
        return val

