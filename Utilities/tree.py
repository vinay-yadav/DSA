from typing import Dict, List, Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CreateBinaryTree:
    def __init__(self) -> None:
        self.treeMap: Dict[int, List[int | None]] = dict()

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        allElements: Set[int] = set()

        for node in descriptions:
            parent, child, isLeftChild = node

            allElements.add(child)
            if self.treeMap.get(parent, None) is None:
                self.treeMap[parent] = [None] * 2

            self.treeMap[parent][isLeftChild ^ 1] = child

        rootNodeValue = [
            element for element in self.treeMap if element not in allElements
        ][0]

        return self.createTree(rootNodeValue)

    def createTree(self, rootValue: int | None) -> Optional[TreeNode]:
        if rootValue is None:
            return

        node = TreeNode(rootValue)

        left = right = None

        children = self.treeMap.get(rootValue, None)
        if children:
            left, right = children

        node.left = self.createTree(left)
        node.right = self.createTree(right)

        return node


def inOrderTraversal(rootNode: Optional[TreeNode]) -> List:
    if rootNode is None:
        return []

    inOrderElements = list()

    inOrderElements.extend(inOrderTraversal(rootNode=rootNode.left))
    inOrderElements.append(rootNode.val)
    inOrderElements.extend(inOrderTraversal(rootNode=rootNode.right))

    return inOrderElements


def preOrderTraversal(rootNode: Optional[TreeNode]) -> List:
    if rootNode is None:
        return []

    preOrderElements = list()

    preOrderElements.append(rootNode.val)
    preOrderElements.extend(preOrderTraversal(rootNode=rootNode.left))
    preOrderElements.extend(preOrderTraversal(rootNode=rootNode.right))

    return preOrderElements


def postOrderTraversal(rootNode: Optional[TreeNode]) -> List:
    if rootNode is None:
        return []

    postOrderElements = list()

    postOrderElements.extend(postOrderTraversal(rootNode=rootNode.left))
    postOrderElements.extend(postOrderTraversal(rootNode=rootNode.right))
    postOrderElements.append(rootNode.val)

    return postOrderElements


def preOrderTraversalIterative(rootNode: Optional[TreeNode]) -> List:
    if rootNode is None:
        return list()

    stack: List[TreeNode] = list()
    preOrderElements: List[int] = list()
    curr: Optional[TreeNode] = rootNode

    while curr is not None or stack:
        while curr is not None:
            preOrderElements.append(curr.val)
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        curr = curr.right

    return preOrderElements


def inOrderTraversalIterative(rootNode: Optional[TreeNode]) -> List:
    if rootNode is None:
        return list()

    stack: List[TreeNode] = []
    inOrderElements: List[int] = list()
    curr: Optional[TreeNode] = rootNode

    while curr is not None or stack:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            inOrderElements.append(curr.val)
            curr = curr.right

    return inOrderElements


def postOrderTraversalIterative(rootNode: Optional[TreeNode]) -> List:
    if rootNode is None:
        return list()

    stack: List[TreeNode] = list()
    lastProcessedNode: Optional[TreeNode] = None
    postOrderElements: List[int] = list()
    curr = rootNode

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        peek: TreeNode = stack[-1]
        if peek.right and lastProcessedNode != peek.right:
            curr = peek.right
        else:
            postOrderElements.append(peek.val)
            lastProcessedNode = stack.pop()

    return postOrderElements


if __name__ == "__main__":
    descriptions = [
        [1, 2, 1],
        [1, 10, 0],
        [2, 4, 1],
        [2, 5, 0],
        [4, 8, 1],
        [5, 6, 1],
        [5, 7, 0],
        [10, 11, 1],
        [10, 12, 0],
    ]

    rootNode = CreateBinaryTree().createBinaryTree(descriptions=descriptions)
    # print("inOrderTraversal ->", inOrderTraversal(rootNode=rootNode))
    # print("preOrderTraversal ->", preOrderTraversal(rootNode=rootNode))
    print("postOrderTraversal ->", postOrderTraversal(rootNode=rootNode))

    # pre_recursive = preOrderTraversal(rootNode=rootNode)
    # pre_iterative = preOrderTraversalIterative(rootNode=rootNode)
    # print(pre_iterative, pre_recursive, sep="\n")
    print(postOrderTraversalIterative(rootNode))
