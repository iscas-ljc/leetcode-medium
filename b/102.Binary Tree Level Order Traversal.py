class Solution(object):
    def levelOrder(self, root):
    	if not root:
    		return []
    	a=[]
    	b=[]
    	result=[]
    	temp=[]
    	a.append(root)
    	while a:
    		for i in a:
    			temp.append(i.val)
    			if i.left :
    				b.append(i.left)
    			if i.right :
    				b.append(i.right)
    		a=b
    		b=[]
    		result.append(temp)
    		temp=[]
    	return result