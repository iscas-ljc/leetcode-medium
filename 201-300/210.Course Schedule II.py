class Solution(object):
    def findOrder(self, numCourses, prerequisites):
    	depth=[0]*numCourses #依赖的课程数量
    	relathionship=[[] for i in range(numCourses)] #课程依赖关系
    	for i in prerequisites:
    		depth[i[0]] += 1
    		relathionship[i[1]].append(i[0])
    	courses = set(range(numCourses))
    	flag=True
    	result=[]
    	while flag and len(courses):
    		flag=False
    		removeList=[]
    		for i in courses:
    			if depth[i]==0:
    				for j in relathionship[i]:
    					depth[j] -= 1
    				removeList.append(i)
    				flag=True
    		for i in removeList:
    			result.append(i)
    			courses.remove(i)
    	if len(courses)==0:
    		return result
    	return []