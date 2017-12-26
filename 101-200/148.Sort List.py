class Solution(object):
    def sortList(self, head):
    	if not head or not head.next:
    		return head
    	mid=self.mid(head)
    	lefthead=head
    	righthead=mid.next
    	mid.next=None
    	return self.merge(self.sortList(lefthead),self.sortList(righthead))
    def merge(self,lefthead,righthead):
    	start=ListNode(0)
    	a=start
    	while lefthead and righthead:
    		if lefthead.val < righthead.val:
    			a.next=lefthead
    			lefthead=lefthead.next
    		else:
    			a.next=righthead
    			righthead=righthead.next
    		a=a.next
    	if lefthead:
    		a.next=lefthead
    	elif righthead:
    		a.next=righthead
    	return start.next
    def mid(self,head):
    	if not head:
    		return head
    	slow=head
    	fast=head
    	while fast.next and fast.next.next:
    		slow=slow.next
    		fast=fast.next.next
    	return slow
