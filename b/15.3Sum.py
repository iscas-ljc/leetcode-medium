 class Solution(object):
    def threeSum(self, nums):
    	result=[]
    	nums.sort()
    	for i in range(len(nums)-2):
    		if i-1>=0 and nums[i-1]==nums[i]:
    			continue
    		#保证没有重复
    		first=i+1
    		last=len(nums)-1
    		while first<last:
    			if nums[i]+nums[first]+nums[last]<0:
    				first+=1
    			elif nums[i]+nums[first]+nums[last]>0:
    				last-=1
    			elif nums[i]+nums[first]+nums[last]==0:
    				result.append((nums[i],nums[first],nums[last]))
    				while first<last and nums[first]==nums[first+1]:
    					first+=1
    				while last>first and nums[last]==nums[last-1]:
    					last-=1
    				#再次保证没有重复
    				first+=1
    				last-=1
    		return result