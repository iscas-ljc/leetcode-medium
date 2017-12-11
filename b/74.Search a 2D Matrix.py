class Solution(object):    
	def searchMatrix(self, matrix, target):
		if len(matrix)==0:
			return False        
		col, row = 0, len(matrix) - 1        
		while col < len(matrix[0]) and row >= 0 :            
			if matrix[row][col] > target : row -= 1            
			elif matrix[row][col] < target : col += 1            
			else : return True        
		return False
