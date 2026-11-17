"""
Minimum Changes to Make K Semi-palindromes
"""

from math import inf


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost_memo = [[-1] * (n + 1) for _ in range(n + 1)]
        memo = [[-1] * (k + 1) for _ in range(n + 1)]

        def get_cost(i: int, j: int) -> int:
            if cost_memo[i][j] != -1:
                return cost_memo[i][j]

            length = j - i + 1
            min_cost = inf

            for d in range(1, length):
                if length % d != 0:
                    continue

                cost = 0
                for group in range(d):  # d groups
                    l = i + group
                    r = l + (length // d - 1) * d

                    while l < r:
                        if s[l] != s[r]:
                            cost += 1
                        l += d
                        r -= d

                min_cost = min(min_cost, cost)

            cost_memo[i][j] = min_cost
            return min_cost

        def solve(start: int, k: int) -> int:
            if k == 0:
                return 0 if start == n else inf

            # early return: each piece needs at least 2 characters
            if start + 2 * k > n:
                return inf

            if memo[start][k] != -1:
                return memo[start][k]

            result = inf

            for end in range(start + 1, n):
                # start...end -> 1 piece
                remaining_cost = solve(end + 1, k - 1)

                if remaining_cost == inf:
                    continue

                result = min(result, get_cost(start, end) + remaining_cost)

            memo[start][k] = result
            return result

        return solve(0, k)


if __name__ == "__main__":
    testCases = [
        ("abcac", 2, 1),
        ("abcdef", 2, 2),
        ("aabbaa", 3, 0),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minimumChanges(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
