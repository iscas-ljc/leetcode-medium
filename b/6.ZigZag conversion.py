class Solution:
    def convert(self, s, numRows):
    	if numRows==1:
    		return s
    	if numRows>=len(s):
    		return s 
    	result=[[] for i in range(numRows)]
    	#分配一个numRows个[]的数组
    	resultstring=''
    	row=0
    	for x in s:
    		#遍历s输出至result
    		result[row].append(x)
    		if row==numRows-1:
    			target=-1
    		if row==0:
    			target=1
    		row+=target
    	for i in range(numRows):
    		#resultstring=resultstring.join(result[i])会报错
    		#join'ac'再join'b'，ac就没了
    		#join 是在后边列表的空隙插入前边元素
    		resultstring+=''.join(result[i])
    	return resultstring
