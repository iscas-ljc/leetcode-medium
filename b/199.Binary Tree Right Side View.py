class Solution:
    def rightSideView(self, root):
    	result=[]
    	if not root:
    		return result
    	layer=[root]
    	while layer:
    		for i in range(len(layer)):
    			top=layer.pop(0)
    			if i==0:
    				result.append(top.val)
    			if top.right:
    				layer.append(top.right)
    			if top.left:
    				layer.append(top.left)
    	return result