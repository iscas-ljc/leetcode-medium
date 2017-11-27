class Solution(object):
    def nextPermutation(self, nums):
    	#首先从右向左遍历数组，找到第一个相邻的左<右的数对，记右下标为x，则左下标为x - 1
		#若x > 0，则再次从右向左遍历数组，直到找到第一个大于nums[x - 1]的数字为止，记其下标为y，交换nums[x - 1], nums[y]
		#最后将nums[x]及其右边的元素就地逆置
        size = len(nums)
        for x in range(size - 1, -1, -1):
            if nums[x - 1] < nums[x]:
                break
        if x > 0:
            for y in range(size - 1, -1, -1):
                if nums[y] > nums[x - 1]:
                    nums[x - 1], nums[y] = nums[y], nums[x - 1]
                    break
        for z in range((size - x) / 2):
            nums[x + z], nums[size - z - 1] = nums[size - z - 1], nums[x + z]