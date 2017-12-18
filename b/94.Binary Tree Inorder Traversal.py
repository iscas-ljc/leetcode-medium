class Solution(object):
    def inorderTraversal(self, root):
    	result=[]
    	self.inorder(result,root)
    	return result
    def inorder(self,result,root):
    	if root:
    		self.inorder(result,root.left)
    		result.append(root.val)
    		self.inorder(result,root.right)