class Solution(object):
    def maxProduct(self, nums):
    	lenn=len(nums)
    	result=max(nums)
    	maxnum=[0]*lenn
    	minnum=[0]*lenn
    	if nums[0]>0:
    		maxnum[0]=nums[0]
    	else:
    		minnum[0]=nums[0]
    	for i in range(1,lenn):
    		if nums[i]>0:
    			maxnum[i]=max(nums[i],maxnum[i-1]*nums[i])
    			minnum[i]=minnum[i-1]*nums[i]
    		elif nums[i]<0:
    			minnum[i]=min(nums[i],maxnum[i-1]*nums[i])
    			maxnum[i]=minnum[i-1]*nums[i]
    		if maxnum[i]>result:
    			result=maxnum[i]
    	return result