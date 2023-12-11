class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        stored=capacity
        ans=0
        for i,v in enumerate(plants):
            if capacity>=v:
                ans+=1
                capacity-=v
            else:
			# main Logic
                ans+=i+(i+1) 
                capacity=stored-v
        return ans