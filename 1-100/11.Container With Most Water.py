class Solution(object):
    def maxArea(self, height):
    	result=0
    	first=0
    	last=len(height)-1
    	while(first<last):
    		result=max(result,(last-first)*min(height[first],height[last]))
    		#计算面积
    		if(height[first]>=height[last]):
    			last-=1
    		elif(height[first]<height[last]):
    			first+=1
    		#由于短板原理，忽略短板找高板
    	return result