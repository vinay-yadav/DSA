"""
Maximum Element After Decreasing and Rearranging
"""

from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        result = 1

        arr.sort()
        
        if arr[0] != 1:
            arr[0] = 1

        for i in range(1, len(arr)):
            if abs(arr[i - 1] - arr[i]) > 1:
                arr[i] = arr[i- 1] + 1
            
            result = max(result, arr[i])

        print(arr)

        return result


if __name__ == "__main__":
    testCases = [
        ([2, 2, 1, 2, 1], 2),
        ([100, 1, 1000], 3),
        ([1, 2, 3, 4, 5], 5),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maximumElementAfterDecrementingAndRearranging(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
