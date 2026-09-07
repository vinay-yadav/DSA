"""
Distinct Subsequence II
"""


class Solution:
    MOD = 1_000_000_007

    def distinctSubseqII(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        n = len(s)
        dp = [-1] * 2001

        prev = [0] * (n + 1)
        lastSeen = [0] * 26
        for i in range(1, n + 1):
            idx = ord(s[i - 1]) - ord("a")
            prev[i] = lastSeen[idx]
            lastSeen[idx] = i

        def countSubsquence(n) -> int:
            if n == 0:
                return 1

            if dp[n] != -1:
                return dp[n]

            total = (2 * countSubsquence(n - 1)) % self.MOD

            if prev[n] != 0:
                duplicates = countSubsquence(prev[n] - 1)
                total = (total - duplicates + self.MOD) % self.MOD

            dp[n] = total
            return dp[n]

        return (countSubsquence(len(s)) - 1 + self.MOD) % self.MOD

    def naive(self, s: str) -> int:
        """
        TC: O(2 ^ n)
        SC: O(2 ^ n)
        """
        n = len(s)
        temp_set = set()

        def backtracking(idx, temp_list):
            if idx == n:
                if len(temp_list) > 0:
                    temp_set.add("".join(temp_list))
                return

            temp_list.append(s[idx])
            backtracking(idx + 1, temp_list)

            temp_list.pop()
            backtracking(idx + 1, temp_list)

        backtracking(0, [])

        return len(temp_set)


if __name__ == "__main__":
    testCases = [
        ("abc", 7),
        ("aba", 6),
        ("aaa", 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().distinctSubseqII(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
