from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))

'''
class Solution(object):  
    def combine(self, n, k):  
        """ 
        :type n: int 
        :type k: int 
        :rtype: List[List[int]] 
        """  
        res = []  
        self.rec(res, 0, n, k, [])  
        return res  
    def rec(self, res, i, n, k, temp) :  
        if k == 0 :  
            res.append(temp)  
            return  
        for j in range(i+1, n+1) :  
            self.rec(res, j, n, k-1, temp+[j]) 