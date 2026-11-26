class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left,count = 0,0
        snum = str(num)
        for right in range(k, len(snum)+1):
            win_int = int(snum[left:right])
            if win_int !=0 and num % win_int ==0:
                count+=1
            left+=1
        return count

