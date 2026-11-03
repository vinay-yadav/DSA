"""
Minimum Moves to Equal Array Elements III
"""


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        max_element = max(nums)

        moves = 0
        for num in nums:
            moves += max_element - num

        return moves


if __name__ == "__main__":
    testCases = [
        ([2, 1, 3], 3),
        ([4, 4, 5], 2),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minMoves(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
