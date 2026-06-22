"""
Maximum Number of Balloons
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freqDict = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0,
        }

        for chr in text:
            if chr in freqDict:
                freqDict[chr] += 1

        singleCharFreq = min(freqDict["b"], freqDict["a"], freqDict["n"])
        doubleCharFreq = min(freqDict["l"], freqDict["o"])
        
        return min(singleCharFreq, doubleCharFreq // 2)

if __name__ == "__main__":
    testCases = [
        ("nlaebolko", 1),
        ("loonbalxballpoon", 2),
        ("leetcode", 0),
        (
            "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw",
            10,
        ),
        ("lloo", 0)
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maxNumberOfBalloons(*inputs)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
