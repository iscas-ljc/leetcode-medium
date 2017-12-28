class Solution(object):
    def findPeakElement(self, nums):
    	lenn=len(nums)
    	return self.search(nums,0,lenn-1)
    def search(self,nums,low,high):
    	if low==high:
    		return low
    	if low+1==high:
    		return [low,high][nums[low]<nums[high]]
    	mid=(low+high)/2
    	if nums[mid]<nums[mid-1]:
    		return self.search(nums,low,mid-1)
    	if nums[mid]<nums[mid+1]:
    		return self.search(nums,mid+1,high)
    	return mid