class Solution(object):
    def generateMatrix(self, n):
    	matrix=[[0 for i in range(n)] for j in range(n)]
    	if len(matrix)==0:
    		return []
    	number=1
    	op=0
    	up=0
    	left=0
    	down=len(matrix)-1
    	right=len(matrix[0])-1
    	while up<=down and left<=right:
    		if op==0:
    			for i in range(left,right+1):
    				matrix[up][i]=number
    				number+=1
    			up+=1
    		if op==1:
    			for i in range(up,down+1):
    				matrix[i][right]=number
    				number+=1
    			right-=1
    		if op==2:
    			for i in range(left,right+1)[::-1]:
    			#倒序排列
    				matrix[down][i]=number
    				number+=1
    			down-=1
    		if op==3:
    			for i in range(up,down+1)[::-1]:
    				matrix[i][left]=number
    				number+=1
    			left+=1
    		op+=1
    		if op>=4:
    			op-=4
    	return matrix
