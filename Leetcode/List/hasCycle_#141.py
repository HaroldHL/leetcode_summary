#Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            # tip:
            # is 判断两个变量是否是引用同一个内存地址。
            # == 判断两个变量是否相等
            if slow is fast:
                return True
        return False 

