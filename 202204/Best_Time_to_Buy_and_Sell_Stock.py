from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0
        min_price: int = max(prices)  # 최댓값을 임시로 넣고 비교하기

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
