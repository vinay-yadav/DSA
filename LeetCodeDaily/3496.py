"""
Maximum Number of Items From Sale I
"""


class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        min_price = float("inf")

        dp = [[-1 for _ in range(budget + 1)] for _ in range(n + 1)]

        copies = [0] * n
        for i in range(n):
            min_price = min(min_price, items[i][1])

            copy = 0
            factor_i = items[i][0]

            for j in range(n):
                if i == j:
                    continue

                factor_j = items[j][0]

                if factor_j % factor_i == 0:
                    copy += 1

            copies[i] += copy

        def knapsack(idx, remaining_budget) -> int:
            if idx < 0:
                return remaining_budget // min_price

            if dp[idx][remaining_budget] != -1:
                return dp[idx][remaining_budget]

            price = items[idx][1]
            pick = 0

            # pick current item
            if remaining_budget >= price:
                pick = 1 + copies[idx] + knapsack(idx - 1, remaining_budget - price)

            # skip current item
            skip = knapsack(idx - 1, remaining_budget)

            ans = max(pick, skip)
            dp[idx][remaining_budget] = ans

            return ans

        return knapsack(n - 1, budget)

    def maximumSaleItems1(self, items: list[list[int]], budget: int) -> int:
        n = len(items)

        min_price = float("inf")
        for _, price in items:
            min_price = min(min_price, price)

        copies = [0] * n
        for i in range(n):
            copy = 0
            factor_i = items[i][0]
            for j in range(n):
                if i == j:
                    continue

                factor_j = items[j][0]

                if factor_j % factor_i == 0:
                    copy += 1

            copies[i] += copy

        def knapsack(idx, remaining_budget, purchased_items) -> int:
            if idx < 0 or remaining_budget < min_price:
                return 0

            _, price = items[idx]

            # pick current item
            item_added = False
            if remaining_budget >= price:
                pick = 1
                if idx not in purchased_items:
                    item_added = True
                    pick += copies[idx]

                purchased_items.add(idx)
                pick += knapsack(idx, remaining_budget - price, purchased_items)
            else:
                pick = 0

            # skip current item
            if item_added:
                purchased_items.remove(idx)

            skip = knapsack(idx - 1, remaining_budget, purchased_items)

            return max(pick, skip)

        return knapsack(n - 1, budget, set())


if __name__ == "__main__":
    testCases = [
        ([[6, 2], [2, 6], [3, 4]], 9, 4),
        ([[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8, 10),
    ]

    for idx, (*inputs, expected) in enumerate(testCases):
        result = Solution().maximumSaleItems(*inputs)  # type: ignore
        status = "Pass" if result == expected else "Fail"
        print(f"Input {idx}: {{{status} -> {result}}}")
