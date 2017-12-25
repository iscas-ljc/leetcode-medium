class Solution(object):
    def preorderTraversal(self, root):
    	self.result=[]
    	self.pre(root)
    	return self.result
    def pre(self,root):
    	if root:
    		self.result.append(root.val)
    		self.pre(root.left)
    		self.pre(root.right)