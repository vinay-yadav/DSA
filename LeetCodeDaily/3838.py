"""
Weighted Word Mapping
"""

from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        wordNum = list()

        for word in words:  # O(n * len(word))
            num = 0
            for char in word:
                num += weights[ord(char) - ord("a")]
            wordNum.append(num % 26)

        for num in wordNum:     # O(n)
            ans += chr(ord('z') - num)

        return ans


if __name__ == "__main__":
    testCases = [
        (
            ["abcd","def","xyz"],
            [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2],
            "rij"
        ),
        (
            ["a","b","c"],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            "yyy"
        ),
        (
            ["abcd"],
            [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5],
            "g"
        )
    ]

    for idx, (words, weights, expected) in enumerate(testCases):
        result = Solution().mapWordWeights(words, weights)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
