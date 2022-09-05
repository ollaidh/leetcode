# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


import my_utils.testing as test


class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return max_profit


if __name__ == '__main__':
    solution = Solution()

    test.run_test(solution.maxProfit, ([2, 1, 2, 1, 0, 1, 2], ), 2, '')
    test.run_test(solution.maxProfit, ([7, 1, 5, 3, 6, 4],), 5, '')
    test.run_test(solution.maxProfit, ([7, 6, 4, 3, 1],), 0, '')
    test.run_test(solution.maxProfit, ([1, 2, 4],), 3, '')

