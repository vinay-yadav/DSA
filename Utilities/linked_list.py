from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional["ListNode"] = None


def createLinkedListFromList(elements: List[int]) -> ListNode:
    for idx, num in enumerate(elements):
        if idx == 0:
            head = curr = ListNode(num)
        else:
            curr.next = ListNode(num)
            curr = curr.next

    return head


def printLinkedList(head: ListNode, returnList: bool = False) -> Optional[List]:
    curr = head
    linkedlist_val = list()

    while curr is not None:
        value = curr.val if returnList else str(curr.val)
        linkedlist_val.append(value)
        curr = curr.next

    if returnList:
        return linkedlist_val
    print(" -> ".join(linkedlist_val))


if __name__ == "__main__":
    linkedListData = [[1, 10, 20], [4, 11, 13], [3, 8, 9]]

    for data in linkedListData:
        head = createLinkedListFromList(data)
        printLinkedList(head)
