"""
Find the Minimum and Maximum Number of Nodes Between Critical Points
"""

from typing import Optional

from Utilities.linked_list import ListNode, createLinkedListFromList

# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        result = [-1, -1]
        if not head or not head.next or not head.next.next:
            return result

        first = head
        second = head.next
        third = second.next

        idx = 2
        firstCriticalIndex = currentCriticalIndex = -1
        minDistance = float("inf")

        while third:
            if first.val > second.val < third.val or first.val < second.val > third.val:
                if firstCriticalIndex == -1:
                    firstCriticalIndex = currentCriticalIndex = idx
                else:
                    minDistance = min(minDistance, idx - currentCriticalIndex)
                    currentCriticalIndex = idx

            first = second
            second = third
            third = third.next
            idx += 1

        if firstCriticalIndex == currentCriticalIndex == -1:
            return result

        if minDistance != float("inf"):
            result[0] = minDistance  # type: ignore
            result[1] = currentCriticalIndex - firstCriticalIndex

        return result


if __name__ == "__main__":
    testCases = [
        ([3, 1], [-1, -1]),
        ([5, 3, 1, 2, 5, 1, 2], [1, 3]),
        ([1, 3, 2, 2, 3, 2, 2, 2, 7], [3, 3]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        head = createLinkedListFromList(*inputs)
        result = Solution().nodesBetweenCriticalPoints(head)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
