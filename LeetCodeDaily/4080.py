"""
Design Bus Seat Booking System
"""


class BusBooking:
    NEIGHBOR = {0: 1, 3: 2}  # A->B, D->C

    def __init__(self, n: int):
        self.cost = [[0] * 4 for _ in range(n)]  # 0 = free, else cost paid at booking
        self.total = 0
        self.count = 0

    def toggle(self, seat: str) -> None:
        col, row = ord(seat[0]) - ord("A"), int(seat[1:]) - 1
        paid = self.cost[row][col]

        if paid:  # already booked -> free it, refund what it cost
            self.total -= paid
            self.count -= 1
            self.cost[row][col] = 0
            return

        c = 1

        # if col == 0 and self.cost[row][1]:
        #     c = 3
        # elif col == 3 and self.cost[row][2]:
        #     c = 3

        if col in self.NEIGHBOR and self.cost[row][self.NEIGHBOR[col]]:
            c = 3

        self.cost[row][col] = c
        self.total += c
        self.count += 1

    def getTotalTime(self) -> int:
        return self.total

    def getMinTime(self) -> int:
        return self.count


if __name__ == "__main__":

    def run(ops, args):
        obj, out = None, []
        for op, a in zip(ops, args):
            if op == "BusBooking":
                obj = BusBooking(*a)
                out.append(None)
            else:
                out.append(getattr(obj, op)(*a))
        return out

    examples = [
        (
            [
                "BusBooking",
                "toggle",
                "toggle",
                "getTotalTime",
                "getMinTime",
                "toggle",
                "toggle",
                "getTotalTime",
                "getMinTime",
            ],
            [[20], ["B3"], ["A3"], [], [], ["C3"], ["D3"], [], []],
            [None, None, None, 4, 2, None, None, 8, 4],
        ),
        (
            [
                "BusBooking",
                "toggle",
                "toggle",
                "getTotalTime",
                "toggle",
                "toggle",
                "toggle",
                "getTotalTime",
                "getMinTime",
            ],
            [[10], ["C7"], ["D7"], [], ["D7"], ["C7"], ["D7"], [], []],
            [None, None, None, 4, None, None, None, 1, 1],
        ),
    ]

    for i, (ops, args, expected) in enumerate(examples, 1):
        got = run(ops, args)
        print(f"Example {i}: {'PASS' if got == expected else 'FAIL'}")
        print("  expected:", expected)
        print("  got:     ", got)
