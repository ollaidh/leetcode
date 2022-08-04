# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

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
    buy = Solution()

    if buy.maxProfit([2,1,2,1,0,1,2]) == 2:
        print('[2,1,2,1,0,1,2]', '- test OK')
    else:
        print('[2,1,2,1,0,1,2]', '- test FAILED!,   expected: 2, got:', buy.maxProfit([2,1,2,1,0,1,2]))

    if buy.maxProfit([7, 1, 5, 3, 6 ,4]) == 5:
        print('[7, 1, 5, 3, 6, 4]', '- test OK')
    else:
        print('[7, 1, 5, 3, 6, 4]', '- test FAILED!,   expected: 5, got:', buy.maxProfit([7,1,5,3,6,4]))

    if buy.maxProfit([7, 6, 4, 3, 1]) == 0:
        print('[7,6,4,3,1]', '- test OK')
    else:
        print('[7,6,4,3,1]', '- test FAILED!,   expected: 0, got:', buy.maxProfit([7,6,4,3,1]))

    if buy.maxProfit([1, 2, 4]) == 3:
        print('[1,2,4]', '- test OK')
    else:
        print('[1,2,4]', '- test FAILED!,   expected: 3, got:', buy.maxProfit([1, 2, 4]))