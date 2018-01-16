class Solution(object):
    def hIndex(self, citations):
    	if len(citations)==0:
    		return 0
    	a=sorted(citations,reverse=True)
    	for i in range(len(a)):
    		if i+1>a[i]:
    			return i
    	return len(citations)