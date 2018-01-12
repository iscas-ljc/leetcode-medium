class Solution(object):
    def kthSmallest(self, root, k):
    	self.result=[]
    	self.mid(root)
    	return result[k-1]
    def mid(self,root):
    	if root is None:
    		return 
    	self.mid(root.left)
    	self.result.append(root.val)
    	self.mid(root.right)
