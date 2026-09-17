"""
Find Two Non-overlapping Sub-arrays Each With Target Sum
"""


class Solution:
    INT_MAX = float("inf")

    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        n = len(arr)

        min_best_len_till_idx = [self.INT_MAX] * n
        result = self.INT_MAX
        bestMinLen = self.INT_MAX

        curr_sum = i = j = 0
        while j < n:
            curr_sum += arr[j]

            while i < j and curr_sum > target:
                curr_sum -= arr[i]
                i += 1

            if curr_sum == target:
                length = j - i + 1

                if i > 0 and min_best_len_till_idx[i - 1] != self.INT_MAX:
                    result = min(result, length + min_best_len_till_idx[i - 1])

                bestMinLen = min(bestMinLen, length)

            min_best_len_till_idx[j] = bestMinLen
            j += 1

        return -1 if result == self.INT_MAX else int(result)


if __name__ == "__main__":
    testCases = [
        ([3, 2, 2, 4, 3], 3, 2),
        ([7, 3, 4, 7], 7, 2),
        ([4, 3, 2, 6, 2, 3, 4], 6, -1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minSumOfLengths(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
