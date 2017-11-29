class Solution(object):
    def combinationSum(self, candidates, target):
    	#利用深度优先搜索(dfs)解决问题
    	result=[]
    	candidates.sort()
    	self.dfs(candidates,target,0,[],result)
    	return result
    def dfs(self,candidates,target,index,path,result):
    	if target<0:
    		return 
    	if target==0:
    		result.append(path)
    		return
    	for i in range(index,len(candidates)):
    		self.dfs(candidates,target-candidates[i],i,path+[candidates[i]],result)