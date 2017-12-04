class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
        #每个元素和对应的元素交换
        	for j in range(i):
        		a=matrix[i][j]
        		matrix[i][j]=matrix[j][i]
        		matrix[j][i]=a
        for k in range(n):
        #同一行左右翻转
        	i=0
        	j=n-1
        	while i<j:
        		a=matrix[k][i]
        		matrix[k][i]=matrix[k][j]
        		matrix[k][j]=a
        		i+=1
        		j-=1