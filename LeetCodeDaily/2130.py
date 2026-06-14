"""
Maximum Twin Sum of a Linked List
"""

from typing import Optional

from Utilities.linked_list import ListNode, createLinkedListFromList


class Solution:
    # SC: O(n)
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        root = head

        linkedListDict = dict()

        while root is not None:
            linkedListDict[n] = root
            n += 1
            root = root.next

        maxTwinSum = 0

        for i in range(n // 2):
            twinIdx = n - 1 - i

            pairSum = linkedListDict[i].val + linkedListDict[twinIdx].val
            maxTwinSum = max(maxTwinSum, pairSum)

        return maxTwinSum

    # SC: O(1)
    def approach2(self, head: ListNode) -> int:
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        fast = self.reverseLinkedList(slow.next)
        slow = head

        maxPairSum = 0
        while fast is not None:
            pairSum = slow.val + fast.val
            slow = slow.next if slow is not None else None
            fast = fast.next

            maxPairSum = max(maxPairSum, pairSum)

        return maxPairSum

    def reverseLinkedList(self, head):
        prev = None
        curr = head
        future = head.next if head is not None else None

        while curr is not None:
            curr.next = prev
            prev = curr
            curr = future

            if future is not None:
                future = future.next

        return prev


if __name__ == "__main__":
    testCases = [([5, 4, 2, 1], 6), ([4, 2, 2, 3], 7), ([1, 100000], 100001)]

    for idx, (heads, expected) in enumerate(testCases):
        linkedList = createLinkedListFromList(heads)
        result = Solution().approach2(head=linkedList)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
