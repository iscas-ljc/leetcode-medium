class Solution(object):
    def spiralOrder(self, matrix):
    	if len(matrix)==0:
    		return []
    	result=[]
    	op=0
    	up=0
    	left=0
    	down=len(matrix)-1
    	right=len(matrix[0])-1
    	while up<=down and left<=right:
    		if op==0:
    			for i in range(left,right+1):
    				result.append(matrix[up][i])
    			up+=1
    		if op==1:
    			for i in range(up,down+1):
    				result.append(matrix[i][right])
    			right-=1
    		if op==2:
    			for i in range(left,right+1)[::-1]:
    			#倒序排列
    				result.append(matrix[down][i])
    			down-=1
    		if op==3:
    			for i in range(up,down+1)[::-1]:
    				result.append(matrix[i][left])
    			left+=1
    		op+=1
    		if op>=4:
    			op-=4
    	return result

