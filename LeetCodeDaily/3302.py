"""
Find the Lexicographically Smallest Valid Sequence
"""


class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        i, j = n - 1, m - 1
        right_matched_length = [0] * n
        right_matched = 0
        while i > -1:
            if j > -1 and word1[i] == word2[j]:
                right_matched += 1
                j -= 1

            right_matched_length[i] = right_matched
            i -= 1

        can_change_character = True
        result = []

        i = j = 0
        while i < n and j < m:
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif (
                can_change_character
                and i + 1 < n
                and right_matched_length[i + 1] >= m - j - 1
            ):
                result.append(i)
                j += 1
                can_change_character = False

            i += 1

        if j == m:
            return result

        return []


if __name__ == "__main__":
    testCases = [
        ("vbcca", "abc", [0, 1, 2]),
        ("bacdc", "abc", [1, 2, 4]),
        ("aaaaaa", "aaabc", []),
        ("abc", "ab", [0, 1]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().validSequence(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
