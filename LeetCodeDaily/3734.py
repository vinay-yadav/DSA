"""
Lexicographically Smallest Palindromic Permutation Greater Than Target
"""


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        result = ""
        base = ord("a")
        freq = [0] * 26

        half = len(s) // 2

        for i in range(len(s)):
            idx = ord(s[i]) - base
            freq[idx] += 1

        oddCount = 0
        midChar = ""

        for idx in range(26):
            if freq[idx] % 2 == 1:
                oddCount += 1
                midChar = chr(idx + base)

            freq[idx] //= 2

        if oddCount > 1:
            return ""

        def backtracking(idx, temp_list, greater):
            nonlocal result

            if len(temp_list) == half:
                candidate = "".join(temp_list)
                rightHalf = "".join(temp_list)[::-1]

                if midChar != "":
                    candidate += midChar

                candidate += rightHalf

                if candidate > target:
                    result = candidate
                    return True

                return False

            for i in range(26):
                if freq[i] == 0:
                    continue

                ch = chr(i + base)

                if not greater and ch < target[idx]:
                    continue

                temp_list.append(ch)
                freq[i] -= 1

                is_greater = greater or ch > target[idx]

                if backtracking(idx + 1, temp_list, is_greater):
                    return True

                temp_list.pop()
                freq[i] += 1

            return False

        backtracking(0, [], False)

        return result


if __name__ == "__main__":
    testCases = [
        ("baba", "abba", "baab"),
        ("baba", "bbaa", ""),
        ("abc", "abb", ""),
        ("aac", "abb", "aca"),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().lexPalindromicPermutation(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
