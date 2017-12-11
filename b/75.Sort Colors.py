class Solution(object):
    def sortColors(self, nums):
    	lenn=len(nums)
    	num0=0
    	num1=0
    	num2=0
    	for i in nums:
    		if i==0:
    			num0+=1
    		if i==1:
    			num1+=1
    		if i==2:
    			num2+=1
    	for i in range(lenn):
    		if num0>0:
    			nums[i]=0
    			num0-=1
    			continue
    		if num1>0:
    			nums[i]=1
    			num1-=1
    			continue
    		if num2>0:
    			nums[i]=2
    			num2-=1

