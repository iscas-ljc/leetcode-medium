class Solution(object):
    def minSubArrayLen(self, s, nums):
    	lenn=len(nums)
    	result=lenn+1
    	start=0
    	end=0
    	now_sum=0
    	while end<lenn:
    		while end<lenn and now_sum < s:
    			now_sum += nums[end]
    			end += 1
    		while start < end and now_sum >= s:
    			result = min(result , end-start)
    			now_sum -= nums[start]
    			start += 1
    	if result == lenn + 1:
    		return 0
    	return result