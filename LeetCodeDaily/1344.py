"""
Angle Between Hands of a Clock
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        1 hour   -> 360/12 = 30 degree
        Hour hande moves when minute hand moves as well
            - 60 minutes = 30 degree
            - 1 minute = 30/60 = 0.5 degree
        1 minute -> 360/60 = 6 degree
        """

        hourAngle = (hour % 12) * 30 + (0.5 * minutes)
        minuteAngle = 6 * minutes

        angle = abs(hourAngle - minuteAngle)

        """ min is used to get min angle if actue angle is greater than obsolute """
        return min(angle, 360 - angle)


if __name__ == "__main__":
    testCases = [(12, 30, 165), (3, 30, 75), (3, 15, 7.5)]

    for idx, (hour, minutes, expected) in enumerate(testCases):
        result = Solution().angleClock(hour, minutes)
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: [{status} -> {result}]")
