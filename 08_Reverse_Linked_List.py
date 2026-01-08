class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head    # Current node we're processing
        prev = None    # Previous node (starts as None)
        
        while temp is not None:
            front = temp.next     # Store next node before we lose it
            temp.next = prev      # Reverse the link: point to previous
            prev = temp           # Move prev pointer forward
            temp = front          # Move current pointer forward
        
        return prev  # prev is now the new head of reversed list