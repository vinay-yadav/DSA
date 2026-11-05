"""
Find the Distance Value Between Two Arrays
"""

import bisect


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        """
        TC: O(nlogm + mlogm)
        SC: O(1)
        """
        n = len(arr2)
        arr2.sort()

        count = 0
        for num in arr1:
            j = bisect.bisect_left(arr2, num)

            if j == 0:
                count += 1 if arr2[0] - num > d else 0
            elif j >= n:
                count += 1 if num - arr2[-1] > d else 0
            else:
                if arr2[j] - num > d and num - arr2[j - 1] > d:
                    count += 1

        return count

    def findTheDistanceValue1(self, arr1: list[int], arr2: list[int], d: int) -> int:
        """
        TC: O(n.m)
        SC: O(1)
        """
        count = 0
        for i in range(len(arr1)):
            all_greater = True
            for j in range(len(arr2)):
                diff = abs(arr1[i] - arr2[j])
                if diff <= d:
                    all_greater = False
                    break

            if all_greater:
                count += 1

        return count


if __name__ == "__main__":
    testCases = [
        ([4, 5, 8], [10, 9, 1, 8], 2, 2),
        ([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3, 2),
        ([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6, 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().findTheDistanceValue(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
