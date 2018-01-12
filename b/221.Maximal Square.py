class Solution(object):
    def maximalSquare(self, matrix):
    	result=0
    	m=len(matrix)
    	if m==0:
    		return 0
    	n=len(matrix[0])
    	dp=[[0]*n for i in range(m)]
    	for i in range(m):
    		for j in range(n):
    			dp[i][j]=int(matrix[i][j])
    			if i>0 and j>0 and dp[i][j]>0:
    				dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
    				#动态规划状态转移方程
    			result=max(result,dp[i][j])
    	return result*result