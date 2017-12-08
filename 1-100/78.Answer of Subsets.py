class Solution(object):
    def subsets(self, nums):  
        """ 
        :type nums: List[int] 
        :rtype: List[List[int]] 
        """  
        result = self.subset_func(nums)  
        for line in result:  
            line.sort()  
        return result  
          
    def subset_func(self,nums):  
        if len(nums)==0:  
            return [[]]  
        if len(nums)==1:  
            return [[],nums]  
        first = nums[0]  
        tmp_nums = nums[1:]  
        tmp_result = self.subset_func(tmp_nums)  
        result = []  
        for key in tmp_result:  
            result.append(key)  
            tmp = list(key)  
            tmp.append(first)  
            result.append(tmp)  
        return result    