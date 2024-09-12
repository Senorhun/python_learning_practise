class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def getMiddle(self, head):
        if head is None:
            return -1
        
        slow = head
        fast = head

        while fast is not None and slow is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data