class Solution(object):
    def rotateRight(self, head, k):
    	if head is None or k==0:
    		return head
    	lenh=1
    	a=head
    	while a.next:
    		a=a.next
    		lenh+=1
    	k%=lenh
    	a.next=head
    	for i in range(lenh-k):
    		a=a.next
    	head=a.next
    	a.next=None
    	return head