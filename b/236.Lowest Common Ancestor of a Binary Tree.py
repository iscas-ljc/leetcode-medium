class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
    	pathp=self.findpath(root,p)
    	pathq=self.findpath(root,q)
    	result=None
    	i=0
    	while i<min(len(pathq),len(pathp)) and pathp[i]==pathq[i]:
    		result=pathp[i]
    		i+=1
    	return result
    def findpath(self,root,target):
    	##!!!重要！！
    	#寻找一个结点在树中的路径
    	path=[]
    	last=None
    	while path or root:
    		if root:
    			path.append(root)
    			root=root.left
    		else:
    			pre=path[-1]
    			if pre.right and last!=pre.right:
    				root=pre.right
    			else:
    				if pre==target:
    					return path
    				last=path.pop()
    				root=None
    	return path