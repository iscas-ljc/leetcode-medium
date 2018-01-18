class Solution(object):
    def majorityElement(self, nums):
    	num1=None
    	num2=None
    	count1=0
    	count2=0
    	result=[]
    	for i in nums:
    		if i==num1:
    			count1+=1
    		elif i==num2:
    			count2+=1
    		elif count1==0:
    			num1=i
    			count1=1
    		elif count2==0:
    			num2=i
    			count2=1
    		else:
    			count1-=1
    			count2-=1
    	if num1 is not None and nums.count(num1)>len(nums)/3:
    		#如果写if num1，那么num1如果是0也会判断为否
    		result.append(num1)
    	if num2 is not None and nums.count(num2)>len(nums)/3:
    		result.append(num2)
    	return result
