MOD = 10**9 +7
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # def isPrime(n):
        #     if n<=1:
        #         return False
        #     for i in range(2, math.sqrt(n)+1):
        #         if n%i ==0:
        #             return False
        #     return True
        even = (n+1)//2
        odd = n//2
        return ((pow(5,even,MOD)) * (pow(4,odd,MOD)))%MOD

        