
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iterative
        # pre,cur = None,head
        # while cur:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        # return pre
        
        # recursive
        # terminator:
        if head== None or head.next==None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return last
if __name__ == "__main__":
    head1 = create_linked_list([1,2,3,4,5])
    print(print_linked_list(Solution().reverseList(head=head1)))

