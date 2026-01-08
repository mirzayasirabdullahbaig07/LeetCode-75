class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge case: single node list
        if not head.next:
            return None  # Delete the only node, return empty list
        
        slow = head          # Slow pointer (tortoise)
        fast = head          # Fast pointer (hare)
        fast = fast.next.next  # Give fast pointer a 2-step head start
        
        # Move pointers until fast reaches the end
        while fast and fast.next:
            slow = slow.next      # Move slow pointer 1 step
            fast = fast.next.next # Move fast pointer 2 steps
        
        # Delete the middle node by skipping it
        slow.next = slow.next.next
        return head