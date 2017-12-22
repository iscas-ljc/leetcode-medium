class Solution(object):
    def flatten(self, root):
    	if root is None:
    		return None
    	self.pre=[]
    	self.preorder(root)
    	if len(self.pre)==1:
    		return 
    	for i in range(len(self.pre)-1):
    		self.pre[i].left=None
    		self.pre[i].right=self.pre[i+1]
    	self.pre[len(self.pre)-1].left=None
    	self.pre[len(self.pre)-1].right=None

    def preorder(self,root):
    	if not root:
    		return 
    	self.pre.append(root)
    	self.preorder(root.left)
    	self.preorder(root.right)