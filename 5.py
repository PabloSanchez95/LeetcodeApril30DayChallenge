class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                print(maxprofit)
                maxprofit += prices[i] - prices[i - 1]

        return maxprofit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 6, 4, 3, 1, 7, 8, 9, 10, 4, 5, 6]))
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
