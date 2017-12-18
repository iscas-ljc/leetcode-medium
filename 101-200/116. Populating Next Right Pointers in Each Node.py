class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
    	if root and root.left and root.right:
    		root.left.next=root.right
    		if root.next is None:
    			root.right.next=None
    		else:
    			root.right.next=root.next.left
    		self.connect(root.left)
    		self.connect(root.right)