class Solution(object):
    def groupAnagrams(self, strs):
    	a=[]
    	b={}
    	result=[]
    	for i in strs:
    		temp=list(i)
    		temp.sort()
    		a.append("".join(temp))
    	for i in range(len(a)):
    	#以排序好的短字符为key建立字典
    		if a[i] not in b:
    			b[a[i]]=[]
    		b[a[i]].append(strs[i])
    	for i in b:
    		result.append(b[i])
    	return result