class Solution(object):
    def pathSum(self, root, sum):
        if root is None:
            return []
    	def dfs(root,target,path):
    		if root.left is None and root.right is None and root.val==target:
    			result.append(path)
    		if root.left:
    			dfs(root.left,target-root.val,path+[root.left.val])
    		if root.right:
    			dfs(root.right,target-root.val,path+[root.right.val])
    	result=[]
    	dfs(root,sum,[root.val])
    	return result