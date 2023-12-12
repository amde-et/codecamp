class Solution:
    def isHappy(self, n: int) -> bool:
        num=str(n)
        sum=0
        seen=[]
        while True:
            for i in num:
                sum+= int(i)**2
            if sum==1:
                return True 
            if sum in seen:
                return False
            seen.append(sum)
            num = str(sum)
            sum=0