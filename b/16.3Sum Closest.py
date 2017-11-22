class Solution(object):
    def threeSumClosest(self, nums, target):
        result=999999
        #为了向小递归，写成nums[0]+nums[1]+nums[2]比较科学
        nums.sort()
        for i in range(len(nums)-2):
            first=i+1
            last=len(nums)-1
            while first<last:
                if nums[i]+nums[first]+nums[last]==target:
                    return target
                if abs(result-target)>abs(nums[i]+nums[first]+nums[last]-target):
                    result=nums[i]+nums[first]+nums[last]
                if nums[i]+nums[first]+nums[last]>target:
                    last-=1
                elif nums[i]+nums[first]+nums[last]<target:
                    first+=1
        return result