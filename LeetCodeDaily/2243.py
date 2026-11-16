"""
Calculate Digit Sum of a String
"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp_list = []
            group_len = group_sum = 0

            for char in s:
                group_sum += int(char)
                group_len += 1

                if group_len == k:
                    temp_list.append(group_sum)
                    group_len = group_sum = 0

            if group_len != 0:
                temp_list.append(group_sum)

            s = "".join([str(i) for i in temp_list])

        return s


if __name__ == "__main__":
    testCases = [
        ("11111222223", 3, "135"),
        ("00000000", 3, "000"),
        ("1234", 2, "37"),
        ("233", 3, "233"),
        ("01234567890", 2, "27"),
        ("9999", 2, "99"),
        ("123", 5, "123"),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().digitSum(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
