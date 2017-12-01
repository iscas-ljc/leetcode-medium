class Solution(object):
    def permute(self, nums):
        return list(itertools.permutations(nums,len(nums)))
        #利用python方法全排列
        #http://blog.csdn.net/mishi_zcf/article/details/52455688