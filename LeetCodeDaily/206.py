"""
Reverse Linked List
"""

from typing import Optional

from Utilities.linked_list import ListNode, createLinkedListFromList, printLinkedList


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev, curr, future = None, head, head.next

        while curr:
            curr.next = prev
            prev = curr
            curr = future

            if future:
                future = future.next
        
        return prev


if __name__ == "__main__":
    testCases = [
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2], [2,1]),
        ([], []),
    ]

    for idx, (heads, expected) in enumerate(testCases):
        if heads:
            linkedList = createLinkedListFromList(heads)
            head = Solution().reverseList(head=linkedList)
            result = printLinkedList(head, True) if head else None
        else:
            result = []

        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
