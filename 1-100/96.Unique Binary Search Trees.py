class Solution(object):
    def numTrees(self, n):
        result=[0]*(n+1)
        result[0]=result[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                result[i]+=result[j-1]*result[i-j]
                #推导的数学公式
        return result[n]