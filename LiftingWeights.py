#TimeComplexity:O(MN) 
#SpaceComplexity: 
#Did this code successfully run on Leetcode : Yes 
#Any problem you faced while coding this : No

class weightLifting():
    def maxWeight(self,weights,maxCapacity):
        dp=[False]*(maxCapacity+1) 
        
        #for i in range(len(weights+1)):
        dp[0]=True
        for i in range(1,len(weights)+1):
            use=[True]*(maxCapacity+1)
            for j in range (1,maxCapacity+1):
                if j>=weights[i-1] and dp[j]==False and dp[j-weights[i-1]]==True and use[j-weights[i-1]]==True:
                    dp[j]=True
                    #use[j-weights[i-1]]=False
                    use[j]=False
        print(dp)
        for i in reversed(range(len(dp))):
            if dp[i]==True:
                return i
       
x=weightLifting()
print(x.maxWeight([5,7,12,18],20))