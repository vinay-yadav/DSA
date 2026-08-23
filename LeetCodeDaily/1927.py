"""
Sum Game
"""


class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left_known_sum, left_q_count = self._sum_and_question_count(num, 0, mid - 1)
        right_known_sum, right_q_count = self._sum_and_question_count(num, mid, n - 1)

        total_q_count = left_q_count + right_q_count

        # Odd total '?' count: Alice always has the decisive last move.
        if total_q_count % 2 == 1:
            return True

        left_score = 2 * left_known_sum + 9 * left_q_count
        right_score = 2 * right_known_sum + 9 * right_q_count

        return left_score != right_score

    def _sum_and_question_count(
        self, num: str, start: int, end: int
    ) -> tuple[int, int]:
        """Return (sum of digits, count of '?') in num[start:end] inclusive."""
        digit_sum = 0
        question_count = 0

        for idx in range(start, end + 1):
            if num[idx] == "?":
                question_count += 1
            else:
                digit_sum += int(num[idx])

        return digit_sum, question_count


if __name__ == "__main__":
    testCases = [
        ("5023", False),
        ("25??", True),
        ("?3295???", False),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().sumGame(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
