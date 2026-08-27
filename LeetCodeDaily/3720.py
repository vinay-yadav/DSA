"""
Lexicographically Smallest Permutation Greater Than Target
"""


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        result = ""
        base = ord("a")
        freq = [0] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - base
            freq[idx] += 1

        def backtracking(idx, temp_list, greater):
            nonlocal result

            if idx == len(target):
                if greater:
                    result = "".join(temp_list)
                    return True
                return False

            for i in range(26):
                ch = chr(i + base)

                if freq[i] == 0:
                    continue

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
        ("abc", "bba", "bca"),
        ("leet", "code", "eelt"),
        ("baba", "bbaa", ""),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().lexGreaterPermutation(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
