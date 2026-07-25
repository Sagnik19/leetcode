class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1   # l = buy day, r = sell day
        maxP = 0

        while r < len(prices):
            # Profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # Found a lower buying price
                l = r

            r += 1

        return maxP

# Time Complexity: O(n)
# Space Complexity: O(1)