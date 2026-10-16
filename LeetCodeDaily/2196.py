"""
Create Binary Tree From Descriptions
"""

from typing import Any, Dict, List, Optional, Set, cast

from Utilities.tree import inOrderTraversal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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


if __name__ == "__main__":
    descriptions = [
        [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]],
        [[1, 2, 1], [2, 3, 0], [3, 4, 1]],
    ]

    for description in descriptions:
        rootNode = Solution().createBinaryTree(description)
        # cast to Any to avoid typing mismatch between local TreeNode and Utilities.tree.TreeNode
        print(inOrderTraversal(cast(Any, rootNode)))
