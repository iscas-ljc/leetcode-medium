import copy
class Solution:
    # 得到回文关系图
    # @param {string} s
    # @return {string[]}
    def getmap(self, s):
        arr=[[False for i in range(len(s))]for j in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if i==j:
                    arr[i][j]=True
                elif s[i]==s[j]:
                    if j==i+1 or arr[i+1][j-1]==True:
                        arr[i][j]=True
        return arr

    # 深度优先搜索
    # @param {string,int,int[],string[],string[][]} s,i,arr,once,result
    def dfs(self,s,i,arr,once,result):
        for j in range(i,len(s)):
            if arr[i][j]==True:
                once.append(s[i:j+1])
                if j+1==len(s):
                    result.append(copy.copy(once)) # attention 2
                self.dfs(s,j+1,arr,once,result)
                once.pop()

    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        # 获得s的回文关系图
        arr = self.getmap(s)
        # result保存最终结果, once保存每个分割, 也就是result的元素
        once = []
        result = []
        self.dfs(s,0,arr,once,result)
        return result