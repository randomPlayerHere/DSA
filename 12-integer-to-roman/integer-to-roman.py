class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        result = ""
        symbol = 0
        while num:
            occur = num // roman[symbol][0]
            result = result + occur * roman[symbol][1]
            num = num % roman[symbol][0]
            symbol +=1
        return result


