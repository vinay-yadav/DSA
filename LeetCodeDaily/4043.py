"""
Count Rotations With Exactly K Equal Adjacent Pairs
"""


class Solution:
    def countRotations(self, s: str, k: int) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        n = len(s)

        result = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                result += 1

        if s[n - 1] == s[0]:
            result += 1

        if result == k:
            return n - result
        elif result - 1 == k:
            return result
        return 0

    def countRotationsI(self, s: str, k: int) -> int:
        """
        TC: O(n^2)
        SC: O(1)
        """
        n = len(s)

        s_list = list(s)

        def rotate(start, end):
            while start < end:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1

        result = 0
        for p in range(n):
            s_list = list(s)
            rotate(0, p)
            rotate(p + 1, n - 1)
            rotate(0, n - 1)

            count = 0
            for i in range(1, n):
                if s_list[i] == s_list[i - 1]:
                    count += 1

            if count == k:
                result += 1

        return result


if __name__ == "__main__":
    testCases = [
        ("aab", 1, 2),
        ("abca", 0, 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countRotations(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
