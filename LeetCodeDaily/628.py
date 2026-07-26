"""
Maximum Product of Three Numbers
"""


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        largest = second_largest = third_largest = float("-inf")
        smallest = second_smallest = float("inf")

        for num in nums:
            # Track the three largest values
            if num > largest:
                third_largest = second_largest
                second_largest = largest
                largest = num
            elif num > second_largest:
                third_largest = second_largest
                second_largest = num
            elif num > third_largest:
                third_largest = num

            # Track the two smallest values
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num

        # Candidate 1: product of the three largest numbers
        product_of_largest = largest * second_largest * third_largest

        # Candidate 2: product of the two smallest (possibly negative)
        # numbers with the single largest number
        product_of_smallest_and_largest = smallest * second_smallest * largest

        return max(product_of_largest, product_of_smallest_and_largest)  # type: ignore


if __name__ == "__main__":
    testCases = [
        # ([1, 2, 3], 6),
        # ([1, 2, 3, 4], 24),
        # ([-1, -2, -3], -6),
        # ([-100, -98, -1, 2, 3, 4], 39200),
        ([-5, -4, -3, -2, 1], 20),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maximumProduct(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
