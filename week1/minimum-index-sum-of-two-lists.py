class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic=dict()
        minVal=2000
        for i in range(len(list1)):
                dic[list1[i]]=i
        
        for i in range(len(list2)):
            if list2[i] in dic:
                dic[list2[i]]+=i
                if dic[list2[i]]==minVal:
                    res.append(list2[i])
                if dic[list2[i]]<minVal:
                    res=[list2[i]]
                    minVal=dic[list2[i]]
        return res

        


        