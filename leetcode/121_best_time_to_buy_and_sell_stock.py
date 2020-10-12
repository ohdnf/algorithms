class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = float('inf')
        for idx, price in enumerate(prices):
            if buy_price > price:
                buy_price = price
                continue
            if max_profit < price - buy_price:
                max_profit = price - buy_price
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]), 5)
