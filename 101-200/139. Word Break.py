class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
'''
超时
class Solution(object):
    def wordBreak(self, s, wordDict):
    	return self.judge(s,wordDict)
    def judge(self,s,wordDict):
    	if s in wordDict:
    		return True
    	for i in range(len(s)):
    		if s[:i] in wordDict:
    			if self.judge(s[i:],wordDict):
    				return True
    	return False
