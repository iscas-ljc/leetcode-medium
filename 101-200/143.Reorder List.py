class Solution(object):
    def reorderList(self, head):
    	if not head:
    		return None
    	#step1：寻找mid
    	slow=head
    	fast=head
    	while fast.next and fast.next.next:
    		slow=slow.next
    		fast=fast.next.next
    	mid=slow

    	#step2:拆分左右两半
    	left=head
    	right=mid.next
    	if right is None:
    		return 
    	mid.next=None

    	#step3:翻转
    	temp=right.next
    	right.next=None
    	while temp:
    		temp2=temp.next
    		temp.next=right
    		right=temp
    		temp=temp2

    	#重新连接
    	temp3=ListNode(0)
    	while left or right:
    		if left is not None:
    			temp3.next=left
    			left=left.next
    			temp3=temp3.next
    		if right is not None:
    			temp3.next=right
    			right=right.next
    			temp3=temp3.next
    	return 