class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tracker={}
        lst1=[]
        for i in nums:
            if i in tracker :
                tracker[i]+=1
            else:
                tracker[i]=1
        for i in tracker:
            if tracker[i] > (len(nums)/3):
                lst1.append(i)
        return lst1
