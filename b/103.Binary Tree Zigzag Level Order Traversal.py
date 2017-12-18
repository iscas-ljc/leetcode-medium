class Solution(object):
    def zigzagLevelOrder(self, root):
    	if not root:
    		return []
    	a=[]
    	b=[]
    	tag=1
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
    		if tag==1:
    			result.append(temp)
    			tag=-1
    		elif tag==-1:
    			result.append(temp[::-1])
    			tag=1
    		temp=[]
    	return result