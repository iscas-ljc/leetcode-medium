class Solution(object):
    def canCompleteCircuit(self, gas, cost):
    	if sum(gas)<sum(cost):
    		return -1
    	result=0
    	remind=0
    	for i in range(len(gas)):
    		remind+=gas[i]
    		remind-=cost[i]
    		if remind<0:
    			result=i+1
    			remind=0
    	return result