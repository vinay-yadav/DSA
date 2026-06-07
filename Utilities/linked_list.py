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


def printLinkedList(head: ListNode) -> None:
    curr = head
    linkedlist_val = list()

    while curr is not None:
        linkedlist_val.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(linkedlist_val))


if __name__ == "__main__":
    linkedListData = [[1, 10, 20], [4, 11, 13], [3, 8, 9]]

    for data in linkedListData:
        head = createLinkedListFromList(data)
        printLinkedList(head)
