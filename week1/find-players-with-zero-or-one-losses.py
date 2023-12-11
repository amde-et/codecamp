class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dc=defaultdict(lambda:[0,0])
        for a in matches:
            dc[a[0]][0]+=1
            dc[a[1]][1]+=1
        ans=[[],[]]
        for a in dc:
            if(dc[a][1]==0):
                ans[0].append(a)
            if(dc[a][1]==1):
                ans[1].append(a)
        ans[0].sort()
        ans[1].sort()
        return ans