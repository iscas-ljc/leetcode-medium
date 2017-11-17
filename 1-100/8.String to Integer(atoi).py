class Solution(object):
    def myAtoi(self, str):
    	#前面可能有很多空字符
    	#可能出现非数字（见到就返回）
    	Max=0x7FFFFFFF
    	Min=-0x80000000
    	i=0
    	#建立一个索引逐位分析
    	lens=len(str)
    	if lens==0:
    		return 0
    	while i<lens and str[i]==' ':
    		i+=1
    	flag=1
    	if str[i]=='-':
    		flag=-1
    		i+=1
    	elif str[i]=='+':
    		flag=1
    		i+=1
    	result=0
    	while i<lens:
    		if str[i]<'0' or str[i]>'9':
    			return flag*result
    		#见到非法字符后面都不要了
    		num=ord(str[i])-ord('0')
    		if flag==1 and result*10+num>Max:
    			return Max
    		if flag==-1 and flag*(result*10+num)<Min:
    			return Min
    		#每次加完看是否移除
    		result=result*10+num
    		i+=1
    	return result*flag

