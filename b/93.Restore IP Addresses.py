class Solution(object):
    def restoreIpAddresses(self, s):
    	lens=len(s)
    	result=[]
    	def check(s1):
    		if len(s1)==1:
    			return True
    		if len(s1) >1 and s1[0]!= '0' and int(s1)<=255:
    			return True
    		return False
    	for i in range(0,min(lens-3,3)):
    		#要给后面三位留出空间:
    		a=s[:i+1]
    		if not check(a):
    			break
    		for j in range(i+1,min(i+4,lens-2)):
    			b=s[i+1:j+1]
    			if not check(b):
    				break
    			for k in range(j+1,min(j+4,lens-1)):
    				c=s[j+1:k+1]
    				d=s[k+1:]
    				if not check(c):
    					break
    				if not check(d):
    					continue
    				#d不能满足，则把首位给c再判断
    				result.append("{}.{}.{}.{}".format(a,b,c,d))
    	return result 