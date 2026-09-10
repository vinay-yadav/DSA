"""
Count Nodes Equal to Average of Subtree
"""

from Utilities.tree import CreateBinaryTree, TreeNode


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def countNodes(head):
            """
            Returns (subtreeSum, subtreeCount) for the subtree rooted at head.
            """

            nonlocal result

            if not head:
                return 0, 0

            leftSum, leftCount = countNodes(head.left)
            rightSum, rightCount = countNodes(head.right)

            subtreeCount = leftCount + rightCount + 1
            subtreeSum = head.val + leftSum + rightSum

            if subtreeSum // subtreeCount == head.val:
                result += 1

            return subtreeSum, subtreeCount

        countNodes(root)

        return result


if __name__ == "__main__":
    testCases = [
        ([4, 8, 5, 0, 1, None, 6], 5),
        ([1], 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        head = CreateBinaryTree().usingList(*inputs)
        result = Solution().averageOfSubtree(head)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
