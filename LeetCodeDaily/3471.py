"""
Find the Largest Almost Missing Number
"""


class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq = [0] * 51

        if k > n:
            return -1

        temp_set = set()
        for i in range(k):
            if nums[i] not in temp_set:
                temp_set.add(nums[i])
                freq[nums[i]] += 1

        s, e = 1, k
        while e < n:
            temp_set.clear()

            for i in range(s, e + 1):
                if nums[i] not in temp_set:
                    temp_set.add(nums[i])
                    freq[nums[i]] += 1

            s += 1
            e += 1

        num = -1
        for i in range(51):
            if freq[i] != 1:
                continue

            num = max(num, i)

        return num


if __name__ == "__main__":
    testCases = [
        ([3, 9, 2, 1, 7], 3, 7),
        ([3, 9, 7, 2, 1, 7], 4, 3),
        ([0, 0], 1, -1),
        ([0, 0], 2, 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().largestInteger(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
