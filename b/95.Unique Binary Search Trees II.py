class Solution(object):
    def dfs(self,start,end):
    	if start>end:
    		return [None]
    	result=[]
    	for i in range(start,end+1):
    		left=self.dfs(start,i-1)
    		right=self.dfs(i+1,end)
    		for j in left:
    			for k in right:
    				root = TreeNode(i)
    				root.left = j
    				root.right = k
    				result.append(root)
    	return result
    def generateTrees(self, n):
    	if n==0:
    		return []
    	return self.dfs(1,n)
