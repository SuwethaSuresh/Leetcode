class Solution:
    def maximumCount(self,nums):
        pc,nc=0,0
        for i in nums:
            if i>0:
                pc+=1
            elif i<0:
                nc+=1
        ans=max(pc,nc)
        return ans