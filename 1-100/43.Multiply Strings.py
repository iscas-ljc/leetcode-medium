class Solution(object):  
    def multiply(self, num1, num2): 
    	num1=num1[::-1]
    	num2=num2[::-1]
    	#把个位放在首位
    	result=[0 for i in range(len(num1)+len(num2)+1)]
    	result_s=[]
    	for i in range(len(num1)):
    		for j in range(len(num2)):
    			result[i+j]+=int(num1[i])*int(num2[j])
    			#乘法规则
    	for i in range(len(result)):
    		carry=result[i]/10
    		result[i]=result[i]%10
    		if i<len(result)-1:
    			result[i+1]+=carry
    			#处理进位
    		result_s.append(str(result[i]))
    	result_s.reverse()
    	while result_s[0]=='0' and len(result_s)>1:
    		del result_s[0]
    		#处理高位0
    	return ''.join(result_s)