"""
Construct Uniform Parity Array II
"""


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        oddCount = 0
        minEle = float("inf")

        for num in nums1:
            minEle = min(minEle, num)

            if num & 1 == 1:
                oddCount += 1

        if minEle & 1 == 0 and oddCount >= 1:  # type: ignore
            return False

        return True


if __name__ == "__main__":
    testCases = [
        ([1, 4, 7], True),
        ([2, 3], False),
        ([4, 6], True),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().uniformArray(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
