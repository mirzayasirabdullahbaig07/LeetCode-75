class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Empty list or single node - nothing to rearrange

        odd = head          # Pointer for odd-positioned nodes
        even = head.next    # Pointer for even-positioned nodes
        even_head = even    # Remember where even group starts

        # Traverse the list, rearranging odd and even nodes
        while even and even.next:
            odd.next = odd.next.next    # Connect current odd to next odd
            odd = odd.next              # Move odd pointer forward
            even.next = even.next.next  # Connect current even to next even
            even = even.next            # Move even pointer forward

        # Append the even list to the end of the odd list
        odd.next = even_head

        return head