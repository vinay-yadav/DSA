"""
Maximum Product of Two Elements in an Array
"""

import heapq


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        T.C: O(n)
        S.C: O(n)
        """

        heap = [num * -1 for num in nums]
        heapq.heapify(heap)

        largest = heapq.heappop(heap) * -1
        second_largest = heapq.heappop(heap) * -1

        return (largest - 1) * (second_largest - 1)

    def maxProduct1(self, nums: list[int]) -> int:
        """
        T.C: O(n)
        S.C: O(1)
        """

        largest = second_largest = 0

        for num in nums:
            if num > largest:
                largest, second_largest = num, largest

            elif num > second_largest:
                second_largest = num

        return (largest - 1) * (second_largest - 1)


if __name__ == "__main__":
    testCases = [
        ([3, 4, 5, 2], 12),
        ([1, 5, 4, 5], 16),
        ([3, 7], 12),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxProduct(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
