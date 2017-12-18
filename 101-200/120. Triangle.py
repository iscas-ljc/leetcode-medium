class Solution(object):
    def minimumTotal(self, triangle):
    	m=len(triangle)
    	if m==0:
    		return 0
    	n=len(triangle[0])
    	result=0
    	for i in range(1,m):
    		for j in range(i+1):
    			if j!=0 and j!=i:
    				triangle[i][j]=min(triangle[i][j]+triangle[i-1][j],triangle[i][j]+triangle[i-1][j-1])
    			if j==0:
    				triangle[i][j]=triangle[i][j]+triangle[i-1][j]
    			if j==i:
    				triangle[i][j]=triangle[i][j]+triangle[i-1][j-1]
    	if max(triangle[len(triangle)-1])<0:
    		return max(triangle[len(triangle)-1])
    	return min(triangle[len(triangle)-1])
