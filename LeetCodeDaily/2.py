"""
Add Two Numbers
"""

from typing import Optional

from Utilities.linked_list import ListNode, createLinkedListFromList, printLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        resultNode = temp3 = None

        temp1, temp2 = l1, l2

        self.carryForward = 0
        while temp1 and temp2:
            tempNode = self.getNewNodeFromSum(temp1.val, temp2.val)

            if resultNode is None:
                temp3 = tempNode
                resultNode = temp3
            else:
                temp3.next = tempNode
                temp3 = temp3.next

            temp1 = temp1.next
            temp2 = temp2.next

        while temp1:
            tempNode = self.getNewNodeFromSum(temp1.val)
            temp3.next = tempNode
            temp3 = temp3.next

            temp1 = temp1.next

        while temp2:
            tempNode = self.getNewNodeFromSum(temp2.val)
            temp3.next = tempNode
            temp3 = temp3.next

            temp2 = temp2.next

        if self.carryForward != 0:
            temp3.next = ListNode(self.carryForward)
            temp3 = temp3.next

        return resultNode

    def getNewNodeFromSum(self, num1, num2=0):
        tempSum = num1 + num2 + self.carryForward

        if tempSum > 9:
            self.carryForward = tempSum // 10
            tempSum %= 10
        else:
            self.carryForward = 0

        return ListNode(tempSum)


if __name__ == "__main__":
    testCases = [
        ([2, 4, 9], [5, 6, 4, 9], [7, 0, 4, 0, 1]),
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ]

    for idx, (l1, l2, expected) in enumerate(testCases):
        l1, l2 = createLinkedListFromList(l1), createLinkedListFromList(l2)
        result = Solution().addTwoNumbers(l1, l2)  # type: ignore
        if result is not None:
            result = printLinkedList(result, True)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
