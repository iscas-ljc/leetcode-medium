class Solution(object):
    def reverseWords(self, s):
    	a=s.split()
    	return " ".join (a[::-1])