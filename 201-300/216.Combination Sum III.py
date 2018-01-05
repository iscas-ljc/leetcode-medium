class Solution(object):
    def combinationSum3(self, k, n):
    	result=[]
    	def search(start,count,sums,nums):
    		if count<0 and sums<0:
    			return 
    		if count==0 and sums==0:
    			result.append(nums)
    			return 
    		for i in range(start+1,10):
    			search(i,count-1,sums-i,nums+[i])
    	search(0,k,n,[])
    	return result