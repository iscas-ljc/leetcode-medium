class Solution:
    def insertionSortList(self, head):
    	if head is None:
    		return None
    	pre=ListNode(0)
    	pre.next=head
    	now=head
    	while now.next:
    		if now.val > now.next.val:
    			a=pre
    			while a.next.val<now.next.val:
    				a=a.next
    			temp=now.next
    			now.next=temp.next
    			temp.next=a.next
    			a.next=temp
    		else:
    			now=now.next
    	return pre.next

'''
直接插入，超时
class Solution(object):
    def insertionSortList(self, head):
    	start=ListNode(0)
    	now=head
    	while now :
    		b=now.next
    		now.next=None
    		a=start
    		while a:
    			if a.next is None or now.val<a.next.val:
    				now.next=a.next
    				a.next=now
    				break
    			a=a.next
    		now=b
    	return start.next
'''