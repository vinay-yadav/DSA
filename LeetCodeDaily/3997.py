"""
Count Dominant Nodes in a Binary Tree
"""

from Utilities.tree import CreateBinaryTree, TreeNode


class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        _, dominantNodeCount = self.processTree(root)

        return dominantNodeCount

    def processTree(self, root) -> tuple[int, int]:
        """
        return: (maxRootValue, dominantNodeCount)
        """
        if root is None:
            return (0, 0)

        leftChildVal, leftDominantCount = self.processTree(root.left)
        rightChildVal, rightDominantCount = self.processTree(root.right)

        dominantNodeCount = leftDominantCount + rightDominantCount

        maxRootVal = max(root.val, leftChildVal, rightChildVal)

        if maxRootVal == root.val:
            dominantNodeCount += 1

        return maxRootVal, dominantNodeCount


if __name__ == "__main__":
    testCases = [
        (
            [
                [5, 3, True],
                [5, 8, False],
                [3, 2, True],
                [3, 4, False],
                [8, 7, True],
                [8, 1, False],
            ],
            5,
        )
        # ([5, 3, 8, 2, 4, 7, 1], 5),
        # ([1, 2, 3, 1, 2], 4)
    ]

    for idx, (treeData, expected) in enumerate(testCases):
        root = CreateBinaryTree().usingList(treeData)
        result = Solution().countDominantNodes(root)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
