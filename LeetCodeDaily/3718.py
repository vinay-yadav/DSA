"""
Smallest Missing Multiple of K
"""


class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        temp_nums = set(nums)

        t = k
        while t in temp_nums:
            t += k

        return t


if __name__ == "__main__":
    testCases = [
        ([8, 2, 3, 4, 6], 2, 10),
        ([1, 4, 7, 10, 15], 5, 5),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().missingMultiple(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
