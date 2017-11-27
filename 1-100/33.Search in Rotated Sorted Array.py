class Solution(object):
    def search(self, nums, target):
        lenn=len(nums)
        for i in range(lenn):
            if nums[i]==target:
                return i
        return -1