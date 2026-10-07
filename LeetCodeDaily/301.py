"""
Remove Invalid Parentheses
"""


class Solution:
    """
    TC: O(2^p)
    SC: O(n)
    """

    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        result = set()
        best = 0  # max number of parentheses kept in any valid string so far

        def backtrack(idx: int, balance: int, path: list[str], kept: int) -> None:
            nonlocal best

            # Prefix has more ')' than '(' -> can never become valid
            if balance < 0:
                return

            if idx == n:
                # `>=` keeps ties; because we try "keep" before "skip",
                # the first valid leaf already has the max kept count,
                # so a strictly greater count never appears later.
                if balance == 0 and kept >= best:
                    best = kept
                    result.add("".join(path))
                return

            char = s[idx]

            if char in "()":
                # +1 for '(', -1 for ')': the only difference between the branches
                delta = 1 if char == "(" else -1

                # Choice 1: keep this parenthesis (must be tried first)
                path.append(char)
                backtrack(idx + 1, balance + delta, path, kept + 1)
                path.pop()  # undo the keep

                # Choice 2: remove this parenthesis
                backtrack(idx + 1, balance, path, kept)
            else:
                # Letters are mandatory: always keep, never branch
                path.append(char)
                backtrack(idx + 1, balance, path, kept)
                path.pop()  # undo, so the shared list is unchanged on exit

        backtrack(0, 0, [], 0)
        return sorted(result)

    def removeInvalidParentheses1(self, s: str) -> list[str]:
        n = len(s)
        result = set()

        best = 0

        def backtracking(idx: int, balance: int, temp_list: list[str], selected: int):
            nonlocal best

            if balance < 0:
                return

            if idx == n:
                if balance == 0 and selected >= best:
                    best = selected
                    result.add("".join(temp_list))
                return

            char = s[idx]
            idx += 1

            if char == "(":
                temp_list.append(char)
                backtracking(idx, balance + 1, temp_list, selected + 1)

                temp_list.pop()
                backtracking(idx, balance, temp_list, selected)
            elif char == ")":
                temp_list.append(char)
                backtracking(idx, balance - 1, temp_list, selected + 1)

                temp_list.pop()
                backtracking(idx, balance, temp_list, selected)
            else:
                temp_list.append(char)
                backtracking(idx, balance, temp_list, selected)
                temp_list.pop()

        backtracking(0, 0, [], 0)

        return sorted(result)


if __name__ == "__main__":
    testCases = [
        ("()())()", ["(())()", "()()()"]),
        ("(a)())()", ["(a())()", "(a)()()"]),
        (")(", [""]),
        ("(a", ["a"]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().removeInvalidParentheses(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
