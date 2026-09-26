"""
Evaluate the Bracket Pairs of a String
"""


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)

        knowledge_dict = dict()
        for key, value in knowledge:
            knowledge_dict[key] = value

        result = []

        idx = 0
        while idx < n:
            if s[idx] == "(":
                idx += 1

                temp_str = []
                while s[idx] != ")":
                    temp_str.append(s[idx])
                    idx += 1

                temp_str = "".join(temp_str)
                temp_str = knowledge_dict.get(temp_str, "?")
                result.append(temp_str)
            else:
                result.append(s[idx])

            idx += 1

        return "".join(result)


if __name__ == "__main__":
    testCases = [
        (
            "(name)is(age)yearsold",
            [["name", "bob"], ["age", "two"]],
            "bobistwoyearsold",
        ),
        ("hi(name)", [["a", "b"]], "hi?"),
        ("(a)(a)(a)aaa", [["a", "yes"]], "yesyesyesaaa"),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().evaluate(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
