class Solution(object):
    def summaryRanges(self, nums):
    	i=0
    	result=[]
    	while i<len(nums):
    		j=i
    		part=str(nums[i])
    		while i+1<len(nums) and nums[i]+1==nums[i+1]:
    			i+=1
    		if i>j:
    			part+='->'+str(nums[i])
    		result.append(part)
    		i+=1
    	return result