class Solution(object):
    def permuteUnique(self, nums):
        a=list(itertools.permutations(nums,len(nums)))
        result=[]
        for i in a:
            if not i in result:
                result.append(i)
        return result