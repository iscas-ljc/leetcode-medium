class Solution(object):
    def divide(self, dividend, divisor):
    	#用被除数减多倍的除数，减不了倍数就是商
    	flag=1
    	if (divisor<0 and dividend>0) or (dividend<0 and divisor>0):
    		flag=-1
    		#判断符号
    	divisor=abs(divisor)
    	dividend=abs(dividend)
    	result=0
    	while dividend>=divisor:
    		x=divisor
    		times=1
    		while dividend>=x:
    			dividend-=x
    			result+=times
    			x<<=1
    			times<<=1
    			#利用左移翻倍，避免使用乘法
    	if flag==-1:
    		result=-result
    	if result>2147483647:
    		return 2147483647
    	if result<-2147483648:
    		return -2147483648
    	return result