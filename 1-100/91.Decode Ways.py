class Solution(object):
    def numDecodings(self, s):
    	lens=len(s)
    	if lens==0:
    		return 0
    	if s[0]=='0':
    		return 0
    	result=[0]*lens
    	result[0]=1
    	if lens==1:
    		return result[0]
    	if lens>=2:
    		if s[1]=='0':
    			if s[0]!='1' and s[0]!='2':
    				return 0
    			result[1]=1
    		elif s[0]=='1':
    			result[1]=2
    		elif s[0]=='2' and s[1]<='6':
    			result[1]=2
    		else:
    			result[1]=1
    	for i in range(2,lens):
    		if s[i]=='0' :
    			if s[i-1] != '1' and s[i-1] != '2':
    				return 0
    			else:
    				result[i]=result[i-2]
    		elif s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6'):
    			result[i]=result[i-1]+result[i-2]
    		else:
    			result[i]=result[i-1]
    	return result[lens-1]
