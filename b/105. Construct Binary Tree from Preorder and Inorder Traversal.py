class Solution(object):
    def buildTree(self, preorder, inorder):
    	if not preorder or not inorder or len(preorder)!=len(inorder):
    		return None
    	root=TreeNode(preorder[0])
    	number=inorder.index(preorder[0])
    	root.left=self.buildTree(preorder[1:1+number],inorder[0:number])
    	root.right=self.buildTree(preorder[number+1:],inorder[number+1:])
    	return root