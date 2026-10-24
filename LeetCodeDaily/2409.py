"""
Count Days Spent Together
"""

from functools import reduce


class Solution:
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        arrival_month, arrival_day = self.last_arrival(arriveAlice, arriveBob)
        departure_month, departure_day = self.first_depart(leaveAlice, leaveBob)

        # if months are same
        if arrival_month == departure_month:
            return max(0, departure_day - arrival_day + 1)

        # if months are different
        if arrival_month > departure_month:
            return 0

        remaining_days_first_month = (
            self.DAYS_IN_MONTH[arrival_month - 1] - arrival_day + 1
        )
        remaining_days_second_month = departure_day

        # calculte days between months
        days = reduce(
            lambda acc, month: acc + self.DAYS_IN_MONTH[month - 1],
            range(arrival_month + 1, departure_month),
            0,
        )

        return remaining_days_first_month + remaining_days_second_month + days

    def last_arrival(self, arriveAlice, arriveBob):
        alice = tuple(map(int, arriveAlice.split("-")))
        bob = tuple(map(int, arriveBob.split("-")))
        return max(alice, bob)

    def first_depart(self, leaveAlice, leaveBob):
        alice = tuple(map(int, leaveAlice.split("-")))
        bob = tuple(map(int, leaveBob.split("-")))
        return min(alice, bob)


if __name__ == "__main__":
    testCases = [
        ("08-15", "08-18", "08-16", "08-19", 3),
        ("10-01", "10-31", "11-01", "12-31", 0),
        ("08-15", "09-18", "08-16", "09-19", 34),
        ("03-05", "07-14", "04-14", "09-21", 92),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().countDaysTogether(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
