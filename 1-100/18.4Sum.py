class Solution(object):
    def fourSum(self, nums, target):
    	def Nsum(nums,target,N,result,results):
    		if len(nums)<N or N<2 or nums[0]*N>target or target >nums[-1]*N:
    			return 
    		#确定一些不用执行直接返回的条件
    		if N==2:
    		#对2个数相加的情况具体处理，其他情况递归
    			first=0
    			last=len(nums)-1
    			while first<last:
    				if nums[first]+nums[last]==target:
    					results.append(result+[nums[first],nums[last]])
    					first+=1
    					while first<last and nums[first]==nums[first-1]:
    						first+=1
    				if nums[first]+nums[last]<target:
    					first+=1
    				if nums[first]+nums[last]>target:
    					last-=1
    		else:
    		#N>2的情况
    			for i in range(len(nums)-N+1):
    				if i==0 or (i>0 and nums[i-1] != nums[i]):
    					Nsum(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)
    	results=[]
    	Nsum(sorted(nums),target,4,[],results)
    	#将排序好的进行N=4的寻找
    	return results