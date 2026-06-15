"""
Delete the Middle Node of a Linked List
"""

from typing import Optional

from Utilities.linked_list import ListNode, createLinkedListFromList, printLinkedList


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        temp = None
        slow = fast = head

        while fast.next is not None and fast.next.next is not None:
            temp = slow
            slow = slow.next if slow else None
            fast = fast.next.next

        if fast.next is not None:
            temp = slow.next
            slow.next = temp.next
            temp.next = None
        else:
            temp.next = slow.next
            slow.next = None

        del temp

        return head


if __name__ == "__main__":
    testCases = [
        ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
        ([1, 2, 3, 4], [1, 2, 4]),
        ([2, 1], [2]),
    ]

    for idx, (heads, expected) in enumerate(testCases):
        linkedList = createLinkedListFromList(heads)
        head = Solution().deleteMiddle(head=linkedList)
        result = printLinkedList(head, True) if head else None

        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
