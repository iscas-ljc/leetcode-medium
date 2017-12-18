class Solution(object):
    def isValidBST(self, root):
    	if root is None:
    		return True
    	self.result=[]
    	self.pre(root)
    	for i in range(1,len(self.result)):
    		if self.result[i]<=self.result[i-1]:
    			return False
    	return True
    def pre(self,root):
    	if root is None:
    		return 
    	self.pre(root.left)
    	self.result.append(root.val)
    	self.pre(root.right)