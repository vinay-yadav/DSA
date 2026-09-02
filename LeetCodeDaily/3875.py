"""
Construct Uniform Parity Array I
"""


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True


if __name__ == "__main__":
    testCases = [
        ([2, 3], True),
        ([4, 6], True),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().uniformArray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
