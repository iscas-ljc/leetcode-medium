class Solution(object):
    def searchRange(self, nums, target):
        lenn=len(nums)
        start=-1
        end=-1
        for i in range(lenn):
            if target==nums[i] and start==-1:
                start=i
            if target==nums[i] and start!=-1:
                end=i
        return [start,end]