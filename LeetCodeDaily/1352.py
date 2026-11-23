"""
Product of the Last K Numbers
"""


class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  # window reaches the last zero
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]


if __name__ == "__main__":

    def run(ops, args):
        obj, out = None, []
        for op, a in zip(ops, args):
            if op == "ProductOfNumbers":
                obj = ProductOfNumbers()
                out.append(None)
            else:
                out.append(getattr(obj, op)(*a))
        return out

    testCases = [
        (
            [
                "ProductOfNumbers",
                "add",
                "add",
                "add",
                "add",
                "add",
                "getProduct",
                "getProduct",
                "getProduct",
                "add",
                "getProduct",
            ],
            [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]],
            [None, None, None, None, None, None, 20, 40, 0, None, 32],
        ),
    ]

    for i, (ops, args, expected) in enumerate(testCases, 1):
        got = run(ops, args)
        print(f"Example {i}: {'PASS' if got == expected else 'FAIL'}")
        print("  expected:", expected)
        print("  got:     ", got)
