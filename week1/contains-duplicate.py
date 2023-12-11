class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tracker={}
        for i in nums:
            if i in tracker:
                tracker[i]+=1
            if i not in tracker:
                tracker[i]=1
        for i in tracker:
            if tracker[i]>=2:
                return True 
        return False 
        