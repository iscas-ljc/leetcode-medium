class Solution(object):
    def uniquePaths(self, m, n):
    	path=[[0 for i in range(n)] for j in range(m)]
    	for i in range(m):
    		path[m][0]=1
    	for i in range(n):
    		paht[0][n]=1
    		#第一行列只有一种到法
    	for i in range(1,m):
    		for j in range(1,n):
    			path[m][n]=path[m-1][n]+path[m][n-1]
    			#每一个点都是上边+左边过来的
    	return path[m-1][n-1] 