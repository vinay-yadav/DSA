"""
Reverse Substrings Between Each Pair of Parentheses
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        TC: O(n)
        SC: O(n)
        Approach: Direction Flipping
        """
        n = len(s)

        open_bracket_idx = []
        door = [-1] * n

        for idx, char in enumerate(s):
            if char == "(":
                open_bracket_idx.append(idx)
            elif char == ")":
                coresponding_idx = open_bracket_idx.pop()
                door[idx], door[coresponding_idx] = coresponding_idx, idx

        result = []
        direction = 1
        idx = 0
        while idx < n:
            char = s[idx]

            if char == "(" or char == ")":
                direction *= -1
                idx = door[idx]
            else:
                result.append(char)

            idx += direction

        return "".join(result)

    def reverseParentheses2(self, s: str) -> str:
        """
        TC: O(n^2)
        SC: O(n^2)
        Approach: Stack
        """
        n = len(s)
        stack = []

        idx = 0
        while idx < n:
            if s[idx] == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())

                stack.pop()

                stack.extend(temp)

            else:
                stack.append(s[idx])

            idx += 1

        return "".join(stack)

    def reverseParentheses1(self, s: str) -> str:
        """
        TC: O(n^2)
        SC: O(n^2)
        Approach: Recursion
        """
        n = len(s)

        def _parse_string(idx) -> tuple[int, str]:
            chars = []

            while idx < n and s[idx] != ")":
                if s[idx] == "(":
                    idx, inner_string = _parse_string(idx + 1)
                    chars.append(inner_string[::-1])
                else:
                    while idx < n and s[idx].isalpha():
                        chars.append(s[idx])
                        idx += 1

            if idx < n:
                idx += 1

            return idx, "".join(chars)

        _, result = _parse_string(0)
        return result


if __name__ == "__main__":
    testCases = [
        ("(abcd)", "dcba"),
        ("(u(love)i)", "iloveu"),
        ("(ed(et(oc))el)", "leetcode"),
        ("a(bcdefghijkl(mno)p)q", "apmnolkjihgfedcbq"),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().reverseParentheses(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
