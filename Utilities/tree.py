from collections import deque
from typing import Dict, List, Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CreateBinaryTree:
    def usingInOrderPostOrderTraversal(
        self, inOrder: List[int], postOrder: List[int]
    ) -> Optional[TreeNode]:

        def createBinaryTree(start: int, end: int, rootPos: int) -> Optional[TreeNode]:
            """
            start: starting index of inOrder traversal
            end: end index of postOrder traversal
            rootPos: root position of root of postOrder traversal
            """

            rootValue = postOrder[rootPos]

            if start == end:
                return TreeNode(rootValue)

            inOrderRootIndex = -1
            for i in range(end + 1):
                if inOrder[i] == rootValue:
                    inOrderRootIndex = i
                    break

            root = TreeNode(rootValue)

            root.left = createBinaryTree(
                start, inOrderRootIndex - 1, rootPos - (end - inOrderRootIndex) - 1
            )
            root.right = createBinaryTree(inOrderRootIndex + 1, end, rootPos - 1)

            return root

        n = len(inOrder)
        return createBinaryTree(0, n - 1, n - 1)

    def usingInOrderPreOrderTraversal(
        self, inOrder: List[int], preOrder: List[int]
    ) -> Optional[TreeNode]:

        def createBinaryTree(start: int, end: int, rootPos: int) -> Optional[TreeNode]:
            """
            start: starting index of inOrder traversal
            end: end index of preOrder traversal
            rootPos: root position of root of preOrder traversal
            """

            rootValue = preOrder[rootPos]

            if start == end:
                return TreeNode(rootValue)

            inOrderRootIndex = -1
            for i in range(end + 1):
                if inOrder[i] == rootValue:
                    inOrderRootIndex = i
                    break

            root = TreeNode(rootValue)
            root.left = createBinaryTree(start, inOrderRootIndex - 1, rootPos + 1)
            root.right = createBinaryTree(
                inOrderRootIndex + 1, end, rootPos + (inOrderRootIndex - start) + 1
            )

            return root

        n = len(inOrder)
        return createBinaryTree(0, n - 1, 0)

    def usingList(self, childern: List[List[int]]) -> Optional[TreeNode]:
        """
        children: [[rootValue, childValue, isLeftChild]]
        """

        allElements: Set[int] = set()
        treeMap: Dict[int, List[int | None]] = dict()

        for node in childern:
            parent, child, isLeftChild = node

            allElements.add(child)
            if treeMap.get(parent, None) is None:
                treeMap[parent] = [None] * 2

            treeMap[parent][isLeftChild ^ 1] = child

        rootNodeValue = [element for element in treeMap if element not in allElements][
            0
        ]

        def createTree(rootValue: int | None) -> Optional[TreeNode]:
            if rootValue is None:
                return

            node = TreeNode(rootValue)

            left = right = None

            children = treeMap.get(rootValue, None)
            if children:
                left, right = children

            node.left = createTree(left)
            node.right = createTree(right)

            return node

        return createTree(rootNodeValue)


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


def levelOrderTraversal(rootNode: Optional[TreeNode]) -> List:
    if rootNode is None:
        return list()

    queue = deque([rootNode])

    levelOrderElements = list()

    while queue:
        queuelength = len(queue)
        temp_list = list()

        for _ in range(queuelength):
            element = queue.popleft()
            temp_list.append(element.val)

            if element.left is not None:
                queue.append(element.left)

            if element.right is not None:
                queue.append(element.right)

        levelOrderElements.append(temp_list)

    return levelOrderElements


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

    # rootNode = CreateBinaryTree().usingList(childern=descriptions)
    # assert inOrderTraversal(rootNode) == inOrderTraversalIterative(rootNode), (
    #     "Issue with InOrderTraversal"
    # )
    # assert preOrderTraversal(rootNode) == preOrderTraversalIterative(rootNode), (
    #     "Issue with PreOrderTraversal"
    # )
    # assert postOrderTraversal(rootNode) == postOrderTraversalIterative(rootNode), (
    #     "Issue with PostOrderTraversal"
    # )

    # print(levelOrderTraversal(rootNode))

    rootNode = CreateBinaryTree().usingInOrderPostOrderTraversal(
        inOrder=[6, 4, 7, 2, 5, 1, 10, 3, 12, 11, 13],
        postOrder=[6, 7, 4, 5, 2, 10, 12, 13, 11, 3, 1],
    )

    print("InPost")
    print(inOrderTraversal(rootNode))
    print(postOrderTraversal(rootNode))
    print(preOrderTraversal(rootNode))

    rootNode = CreateBinaryTree().usingInOrderPreOrderTraversal(
        inOrder=[6, 4, 7, 2, 5, 1, 10, 3, 12, 11, 13],
        preOrder=[1, 2, 4, 6, 7, 5, 3, 10, 11, 12, 13],
    )

    print("InPre")
    print(inOrderTraversal(rootNode))
    print(postOrderTraversal(rootNode))
    print(preOrderTraversal(rootNode))
