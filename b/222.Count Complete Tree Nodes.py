class Solution(object):
    def countNodes(self, root):
    	if not root:
    		return 0
    	leftdepth=self.depth(root.left)
    	rightdepth=self.depth(root.right)
    	if leftdepth==rightdepth:
    		return pow(2,rightdepth)+self.countNodes(root.right)
    	elif leftdepth>rightdepth:
    		return pow(2,rightdepth)+self.countNodes(root.left)
    def depth(self,root):
    	if not root:
    		return 0
    	return 1+self.depth(root.left)