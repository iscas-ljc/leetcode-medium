class Solution(object):
    def lengthOfLIS(self, nums):
    	if len(nums)==0:
    		return 0
    	result=[1]*(len(nums))
    	for i in range(len(nums)):
    		for j in range(i):
    			if nums[i]>nums[j]:
    				result[i]=max(result[i],result[j]+1)
    	return max(result)