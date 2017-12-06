class Solution(object):
    def canJump(self, nums):
    	#tips：跳棋可以无限往后走
    	lenn=len(nums)
    	Max=nums[0]
    	for i in range(lenn):
    		if Max<i:
    			#如果中间某个节点都跳不到，直接false
    			return False
    		Max=max(Max,nums[i]+i)
    		#更新最远跳的距离
    	return Max>=lenn-1