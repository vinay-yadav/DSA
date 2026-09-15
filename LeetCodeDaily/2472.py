"""
Maximum Number of Non-overlapping Palindrome Substrings
"""


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """
        TC: O(n^2)
        TC: O(n^2)
        """
        n = len(s)

        if k == 1:
            return n

        dp = [-1 for _ in range(n + 1)]
        for length in range(k):
            dp[length] = 0

        isPalindrome = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        for l in range(1, n + 1):
            i = 0
            while i + l <= n:
                j = i + l - 1

                if i == j:
                    isPalindrome[i][j] = True
                elif i + 1 == j:
                    isPalindrome[i][j] = s[i] == s[j]
                else:
                    isPalindrome[i][j] = s[i] == s[j] and isPalindrome[i + 1][j - 1]

                i += 1

        for length in range(k, n + 1):
            result = dp[length - 1]
            j = length - 1

            i = 0
            while j - i + 1 >= k:
                if isPalindrome[i][j]:
                    result = max(result, 1 + dp[i])
                i += 1

            dp[length] = result

        return dp[n]

    def maxPalindromes1(self, s: str, k: int) -> int:
        """
        TC: O(n^2)
        TC: O(n^2)
        """
        n = len(s)

        if k == 1:
            return n

        dp = [-1 for _ in range(n + 1)]

        isPalindrome = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        for l in range(1, n + 1):
            i = 0
            while i + l <= n:
                j = i + l - 1

                if i == j:
                    isPalindrome[i][j] = True
                elif i + 1 == j:
                    isPalindrome[i][j] = s[i] == s[j]
                else:
                    isPalindrome[i][j] = s[i] == s[j] and isPalindrome[i + 1][j - 1]

                i += 1

        def solve(length):
            if length < k:
                return 0

            if dp[length] != -1:
                return dp[length]

            result = solve(length - 1)

            j = length - 1
            i = 0
            while j - i + 1 >= k:
                if isPalindrome[i][j]:
                    result = max(result, 1 + solve(i))
                i += 1

            dp[length] = result

            return dp[length]

        return solve(n)

    def blueprintBottomUp(self, s: str, k: int) -> int:
        """
        TC: O(n^2)
        TC: O(n^2)
        """
        n = len(s)

        if k == 1:
            return n

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        isPalindrome = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        for l in range(1, n + 1):
            i = 0
            while i + l <= n:
                j = i + l - 1

                if i == j:
                    isPalindrome[i][j] = True
                elif i + 1 == j:
                    isPalindrome[i][j] = s[i] == s[j]
                else:
                    isPalindrome[i][j] = s[i] == s[j] and isPalindrome[i + 1][j - 1]

                i += 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                grow = dp[i][j + 1]
                slide = dp[i + 1][j + 1]

                if isPalindrome[i][j]:
                    take = 1 + dp[j + 1][j + k] if j + k < n else 1
                    dp[i][j] = max(take, grow, slide)

                dp[i][j] = max(dp[i][j], grow, slide)

        return dp[0][k - 1]

    def blueprintTopDown(self, s: str, k: int) -> int:
        """
        TC: O(n^2)
        TC: O(n^3)
        """
        n = len(s)

        if k == 1:
            return n

        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        isPalindrome = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        for l in range(1, n + 1):
            i = 0
            while i + l <= n:
                j = i + l - 1

                if i == j:
                    isPalindrome[i][j] = True
                elif i + 1 == j:
                    isPalindrome[i][j] = s[i] == s[j]
                else:
                    isPalindrome[i][j] = s[i] == s[j] and isPalindrome[i + 1][j - 1]

                i += 1

        def solve(i, j):
            if i >= n or j >= n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            slide = solve(i + 1, j + 1)
            grow = solve(i, j + 1)

            if isPalindrome[i][j]:
                take = 1 + solve(j + 1, j + k)
                dp[i][j] = max(take, slide, grow)
            else:
                dp[i][j] = max(slide, grow)

            return dp[i][j]

        return solve(0, k - 1)

    def naiveBottomUp(self, s: str, k: int) -> int:
        """
        TC: O(n^3)
        TC: O(n^2)
        """
        n = len(s)

        if k == 1:
            return n

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        def isPalindrome(start, end) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1

            return True

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                grow = dp[i][j + 1]
                slide = dp[i + 1][j + 1]

                if isPalindrome(i, j):
                    take = 1 + dp[j + 1][j + k] if j + k < n else 1
                    dp[i][j] = max(take, grow, slide)

                dp[i][j] = max(dp[i][j], grow, slide)

        return dp[0][k - 1]

    def naiveTopDown(self, s: str, k: int) -> int:
        """
        TC: O(n^3)
        TC: O(n^2)
        """
        n = len(s)

        if k == 1:
            return n

        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        def isPalindrome(start, end) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1

            return True

        def solve(i, j):
            if i >= n or j >= n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            slide = solve(i + 1, j + 1)
            grow = solve(i, j + 1)

            if isPalindrome(i, j):
                take = 1 + solve(j + 1, j + k)
                dp[i][j] = max(take, slide, grow)
            else:
                dp[i][j] = max(slide, grow)

            return dp[i][j]

        return solve(0, k - 1)


if __name__ == "__main__":
    testCases = [
        ("abaccdbbd", 3, 2),
        ("adbcda", 2, 0),
        ("cabad", 3, 1),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxPalindromes(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
