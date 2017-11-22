class Solution(object):
    def removeNthFromEnd(self, head, n):
        b=head
        lenh=0
        while b:
            b=b.next
            lenh+=1
        #统计链表长度
        if lenh==1 and n==1:
            return None
        #都为1则都删除 
        n=lenh-n+1
        #逆向转化为正向
        while n==1:
            head=head.next
            return head
        a=head
        while n-2:
            a=a.next
            n-=1
        a.next=a.next.next
        return head