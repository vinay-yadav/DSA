class Solution:
    def solve(self, A, B): ...


if __name__ == "__main__":
    testCases = []

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().solve(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
