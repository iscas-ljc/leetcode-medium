class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        #数学题，再斟酌
        xor = reduce(lambda x, y : x ^ y, nums)
        lowbit = xor & -xor
        a = b = 0
        for num in nums:
            if num & lowbit:
                a ^= num
            else:
                b ^= num
        return [a, b]