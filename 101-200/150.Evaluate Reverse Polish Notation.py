class Solution(object):
    def evalRPN(self, tokens):
    	op=['+','-','*','/']
    	number=[]
    	#建立一个堆栈，反向取数据
    	for token in tokens:
    		if token in op:
    			x=number.pop()
    			y=number.pop()
    			number.append(self.compute(y,x,token))
    		else:
    			number.append(int(token))
    	return number[0]
    def compute(self,x,y,op):
    	return{
    	    '+':lambda x,y:x+y,
    	    '-':lambda x,y:x-y,
    	    '*':lambda x,y:x*y,
    	    '/':lambda x,y:int(float(x) / y),
    	}[op](x,y)
