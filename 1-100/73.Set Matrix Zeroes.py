class Solution(object):
    def setZeroes(self, matrix):
    	m=len(matrix)
    	n=len(matrix[0])
    	row=[]
    	col=[]
    	for i in range(m):
    		for j in range(n):
    			if matrix[i][j]==0:
    				if i not in row:
    					row.append(i)
    				if j not in col:
    					col.append(j)
    	#寻找数组之中的0
    	for i in row:
    		for j in range(n):
    			matrix[i][j]=0
    	for i in col:
    		for j in range(m):
    			matrix[j][i]=0