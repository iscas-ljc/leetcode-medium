class Solution(object):
    def longestPalindrome(self, s):
    	lens=len(s)
    	if lens==0:
    		return 0
    	first=0
    	maxlen=1
    	for i in range(lens):
    		if i-maxlen-1>=0 and s[i-maxlen-1:i+1]==s[i-maxlen-1:i+1][::-1]:
    			#确定最大maxlen，一趟遍历逐步从1更新
    			first=i-maxlen-1
    			maxlen+=2
    			continue
    		if i-maxlen>=0 and s[i-maxlen:i+1]==s[i-maxlen:i+1][::-1]:
    			first=i-maxlen
    			maxlen+=1
    	return s[first:first+maxlen] 