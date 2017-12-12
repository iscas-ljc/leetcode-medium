class Solution:  
    # @param num, a list of integer  
    # @return a list of lists of integer  
    # a dfs problem  
    def dfs(self, res, val, num, start):  
        if val not in res:  
            res.append(val)  
        for i in range(start, len(num)):  
            self.dfs(res, val+[num[i]], num, i+1)  
    def subsetsWithDup(self, S):  
        res = []  
        if len(S) == 0:  
            return res  
        S.sort()  
        val = []  
        self.dfs(res, val, S, 0)  
        return res  