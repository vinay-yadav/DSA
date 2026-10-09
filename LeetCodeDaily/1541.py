"""
Minimum Insertions to Balance a Parentheses String
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        n = len(s)
        required = open_brackets = 0

        idx = 0
        while idx < n:
            char = s[idx]

            if char == "(":
                required += 2
                open_brackets += 1
                idx += 1
                continue

            if open_brackets:
                if idx < n - 1 and s[idx + 1] == char:
                    required -= 2
                    idx += 2
                else:
                    idx += 1
                    required -= 1
                open_brackets -= 1
            else:
                if idx < n - 1 and s[idx + 1] == char:
                    required += 1
                    idx += 2
                else:
                    required += 2
                    idx += 1

        return required

    def minInsertions1(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        n = len(s)
        stack = []
        required = 0
        idx = 0

        while idx < n:
            char = s[idx]

            if char == "(":
                stack.append(char)
                idx += 1
                continue

            # char == ")"
            if stack:
                if idx < n - 1 and s[idx + 1] == char:
                    idx += 2
                else:
                    idx += 1
                    required += 1
                stack.pop()
            else:
                if idx < n - 1 and s[idx + 1] == char:
                    required += 1
                    idx += 2
                else:
                    required += 2
                    idx += 1

        return required + len(stack) * 2


if __name__ == "__main__":
    testCases = [
        ("(()))", 1),
        ("())", 0),
        ("))())(", 3),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().minInsertions(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
