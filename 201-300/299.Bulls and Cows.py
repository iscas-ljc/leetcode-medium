class Solution(object):
    def getHint(self, secret, guess):
    	a=0
    	b=0
    	for i in range(len(secret)):
    		if secret[i] == guess[i]:
    			a+=1
    	x="1234567890"
    	for i in x:
    		b+=min(secret.count(i),guess.count(i))
    	return str(a)+'A'+str(b-a)+'B'