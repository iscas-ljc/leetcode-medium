class Solution(object):
    def sortedListToBST(self, head):
    	if head:
    		pre=ListNode(0)
    		slow=head
    		fast=head
    		while fast and fast.next:
    			pre=slow
    			slow=slow.next
    			fast=fast.next.next
    		root=TreeNode(slow.val)
    		#中间节点作为树的根节点
    		if pre:
    			pre.next=None
    			#截断左边的链表
    			root.left=self.sortedListToBST(head)
    		root.right=self.sortedListToBST(slow.next)
    		return root