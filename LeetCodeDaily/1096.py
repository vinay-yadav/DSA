"""
Brace Expansion II
"""


class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.n = len(expression)
        self.idx = 0
        self.expression = expression

        result: list[str] = []

        st = self.performUnion()
        for s in st:
            result.append(s)

        result.sort()

        return result

    def performUnion(self) -> set:
        result: set = set()

        while True:
            temp: set = self.performConcat()

            for i in temp:
                result.add(i)

            if self.idx < self.n and self.expression[self.idx] == ",":
                self.idx += 1
            else:
                break

        return result

    def performConcat(self) -> set:
        result: set = {""}

        while self.idx < self.n and (
            self.expression[self.idx] == "{" or self.expression[self.idx].isalpha()
        ):
            temp = self.getUnit()

            concatResult = set()
            for left in result:
                for right in temp:
                    concatResult.add(left + right)

            result = concatResult

        return result

    def getUnit(self) -> set:
        result: set = set()

        if self.expression[self.idx] == "{":
            self.idx += 1
            result = self.performUnion()
        else:
            result = {self.expression[self.idx]}

        self.idx += 1

        return result


if __name__ == "__main__":
    testCases = [
        ("{a,b}{c,{d,e}}", ["ac", "ad", "ae", "bc", "bd", "be"]),
        ("{{a,z},a{b,c},{ab,z}}", ["a", "ab", "ac", "z"]),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().braceExpansionII(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
