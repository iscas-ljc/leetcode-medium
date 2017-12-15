class Solution(object):  
    def deleteDuplicates(self, head):  
        """ 
        :type head: ListNode 
        :rtype: ListNode 
        """  
          
        if head is None or head.next is None:  
            return head  
          
        dummy=ListNode(0)  
        dummy.next=head  
        pre=dummy  
        cur=head  
        post=head.next  
          
        while post:  
            while post and post.val != cur.val:                 # 没有重复的时候  
                post=post.next  
                cur=cur.next  
                pre=pre.next  
            while post and post.val==cur.val:                   # 有重复的时候  
                post=post.next  
            if post != cur.next:                                # 只有在有重复的时候这么做  
                pre.next=post  
                cur=post  
                if post is not None:  
                    post=post.next  
              
        return dummy.next 