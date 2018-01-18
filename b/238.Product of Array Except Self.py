class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        #建立一个output[]
        #每个元素=从第1个乘到他左边，再从最后一个乘到他右边
        #O(n)
        size = len(nums)
        output = [1] * size
        left = 1
        for x in range(size - 1):
            left *= nums[x]
            output[x + 1] *= left
        right = 1
        for x in range(size - 1, 0, -1):
            right *= nums[x]
            output[x - 1] *= right
        return output