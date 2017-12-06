class Solution(object):
    def merge(self, intervals):
    	leni=len(intervals)
    	#for i in range(leni):
    	#	for j in range(i+1,leni):
    	#		if intervals[i].start>intervals[j].start:
    	#			intervals[i],intervals[j]=intervals[j],intervals[i]
    	#			冒泡超时
        intervals.sort(key = lambda x: x.start)
        #以start为key排序
    	result=[]
    	i=0
    	while i<leni:
    		a=intervals[i]
    		start=intervals[i].start
    		end=intervals[i].end
    		while i+1<leni and start<=intervals[i+1].start<=a.end:
    			a.end=max(a.end,intervals[i+1].end)
    			#更新end
    			i+=1
    		result.append(a)
    		i+=1
    	return result