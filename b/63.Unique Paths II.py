class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
    	m=len(obstacleGrid)
    	n=len(obstacleGrid[0])
    	path=[[0 for i in range(n)] for j in range(m)]
    	for i in range(m):
    		if obstacleGrid[i][0]==1:
    			break
    		path[i][0]=1
    	for j in range(n):
    		if obstacleGrid[0][j]==1:
    			break
    		path[0][j]=1
    		#确定第一行的可到位置，有障碍就跳出
    	for i in range(1,m):
    		for j in range(1,n):
    			if obstacleGrid[i][j]!=1:
    				path[i][j]=path[i-1][j]+path[i][j-1]
    	return path[m-1][n-1]
