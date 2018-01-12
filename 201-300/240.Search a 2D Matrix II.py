class Solution(object):
    def searchMatrix(self, matrix, target):
    	m=len(matrix)
    	if m==0:
    		return False
    	n=len(matrix[0])
    	if n==0:
    		return False
    	n=n-1
    	for i in range(m):
    		while n and matrix[i][n]>target:
    			n-=1
    		if matrix[i][n]==target:
    			return True
    	return False