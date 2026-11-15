"""
Number of Sub-arrays With Odd Sum
"""


class Solution:
    MOD = 1_000_000_007

    def numOfSubarrays(self, arr: list[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        odd_count = 0
        even_count = 1
        cumm_sum = 0

        subarrays = 0
        for num in arr:
            cumm_sum += num

            if cumm_sum % 2 == 0:
                # even + odd = odd
                subarrays = (subarrays + odd_count) % self.MOD
                even_count += 1
            else:
                # odd + even = odd
                subarrays = (subarrays + even_count) % self.MOD
                odd_count += 1

        return subarrays

    def numOfSubarrays1(self, arr: list[int]) -> int:
        """
        Brute Force
        TC: O(n ^ 2)
        SC: (1)
        """
        n = len(arr)

        subarrays = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]

                if s % 2 == 1:
                    subarrays += 1

        return subarrays


if __name__ == "__main__":
    testCases = [
        ([1, 3, 5], 4),
        ([2, 4, 6], 0),
        ([1, 2, 3, 4, 5, 6, 7], 16),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().numOfSubarrays(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
