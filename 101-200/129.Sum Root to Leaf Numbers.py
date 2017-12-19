class Solution(object):
    def sumNumbers(self, root):
    	self.result=0
    	self.sum(root,0)
    	return self.result
    def sum(self,root,tile_now):
    	if root:
    		self.sum(root.left,tile_now*10+root.val)
    		self.sum(root.right,tile_now*10+root.val)
    		if not root.left and not root.right:
    			self.result+=tile_now*10+root.val