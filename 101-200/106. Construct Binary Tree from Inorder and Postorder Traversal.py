class Solution(object):
    def buildTree(self, inorder, postorder):
    	if not postorder or not inorder or len(postorder)!=len(inorder):
    		return None
    	root=TreeNode(postorder[len(postorder)-1])
    	i=inorder.index(postorder[len(postorder)-1])
    	root.left=self.buildTree(inorder[:i],postorder[:i])
    	root.right=self.buildTree(inorder[i+1:],postorder[i:len(postorder)-1])
    	return root