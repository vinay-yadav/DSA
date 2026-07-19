"""
Remove Duplicate Letters
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        monoStack = list()
        lastSeen = [-1] * 26
        elementUsed = [False] * 26
        base = ord("a")

        for i, ch in enumerate(s):
            idx = ord(ch) - base
            lastSeen[idx] = i

        for i, ch in enumerate(s):
            idx = ord(ch) - base

            if elementUsed[idx]:
                continue

            while monoStack:
                lastElement = monoStack[-1]
                if ord(lastElement) < ord(ch):
                    break

                lastIndex = ord(lastElement) - base
                if lastSeen[lastIndex] < i:
                    break

                monoStack.pop()
                elementUsed[lastIndex] = False

            monoStack.append(ch)
            elementUsed[idx] = True

        return "".join(monoStack)


if __name__ == "__main__":
    testCases = [("bcabc", "abc"), ("cbacdcbc", "acdb")]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().removeDuplicateLetters(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
