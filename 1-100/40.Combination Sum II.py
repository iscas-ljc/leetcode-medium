class Solution(object):
    def combinationSum2(self, candidates, target):
    	#利用深度优先搜索(dfs)解决问题
    	result=[]
    	candidates.sort()
    	self.dfs(candidates,target,0,[],result)
    	result1=[]
    	for i in result:
    	#利用一次循环讲result数组去重
    		if not i in result1:
    			result1.append(i)
    	return result1
    def dfs(self,candidates,target,index,path,result):
    	if target<0:
    		return 
    	if target==0:
    		result.append(path)
    		return
    	for i in range(index,len(candidates)):
    		self.dfs(candidates,target-candidates[i],i+1,path+[candidates[i]],result)
    		#讲i改为i+1则保证了每个数不无限取