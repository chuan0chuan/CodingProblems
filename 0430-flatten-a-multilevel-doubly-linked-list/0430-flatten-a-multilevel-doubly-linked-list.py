"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head

        while curr:
            if not curr.child:
                curr = curr.next
                continue
            
            next_node = curr.next

            child = curr.child
            curr.next = child
            child.prev = curr
            curr.child = None

            tail = child
            while tail.next:
                tail=tail.next
            
            if next_node:
                tail.next = next_node
                next_node.prev = tail
            
            curr = curr.next
    
        return head