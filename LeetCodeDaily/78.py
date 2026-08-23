"""
Subsets
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []

        def backtrack(idx, temp_list):
            if idx == n:
                result.append(temp_list.copy())
                return

            temp_list.append(nums[idx])
            backtrack(idx + 1, temp_list)
            temp_list.pop()
            backtrack(idx + 1, temp_list)

        backtrack(0, [])

        result.sort()  # Optional

        return result


if __name__ == "__main__":
    testCases = [
        ([0], [[], [0]]),
        ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().subsets(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
