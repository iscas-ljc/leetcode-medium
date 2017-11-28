class Solution(object):
    def isValidSudoku(self, board):
    	for i in range(9):
    		#判断每行是不是没有重复
    		a=[0 for x in range(10)]
    		for j in range(9):
    			if board[i][j]=='.':
    				continue
    			num=ord(board[i][j])-ord('0')
    			if a[num]==1:
    				return False
    			a[num]=1
    	for j in range(9)
    		#判断每列是不是没有重复
    		a=[0 for x in range(10)]
    		for i in range(9):
    			if board[i][j]=='.':
    				continue
    			num=ord(board[i][j])-ord('0')
    			if a[num]==1:
    				return False
    			a[num]=1
    	for i in range(0,9,3):
    		for j in range(0,9,3):
    			#判断每个大格是不是没有重复
    			a=[0 for x in range(10)]
    			for p in range(i,i+3):
    				for q in range(j,j+3):
    					if board[p][q]=='.':
    						continue
    					num=ord(board[p][q])-ord('0')
    					if a[num]==1:
    						return False
    					a[num]=1
    	return True

