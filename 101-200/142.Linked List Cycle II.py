class Solution(object):
    def detectCycle(self, head):
    	if not head or not head.next:
    		return None
    	slow=head.next
    	fast=head.next.next
    	while fast and fast.next and slow!=fast:
    		fast=fast.next.next
    		slow=slow.next
    	if not fast or not fast.next:
    		return None
    	slow=head
    	while slow!=fast:
    		slow=slow.next
    		fast=fast.next.next
    	return slow
'''
需要额外空间
class Solution(object):
    def detectCycle(self, head):
    	s=[]
    	while head:
    		s.append(s)
    		head=head.next
    		if head in s:
    			return head
    	return None
