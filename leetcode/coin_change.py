class Solution(object):
    def useCoin(self, coins, amount, num):
        if amount == 0:
            return num
        # reduction = -1
        for i in xrange(len(coins)):
            if coins[i] <= amount:
                # amount -= coins[i]
                result = self.useCoin(coins[i:], amount - coins[i], num+1)
                if result != -1:
                    print coins[i]
                    return result
        return -1
                # reduction = i
        # if reduction != -1:
        #     for i 
        # else:
        #     return -1

    def count(self, coins, m, n):
        print m, n
        if n == 0:
            return 1
        elif n < 0:
            return 0

        if m >= len(coins):
            return 0
        havethis = self.count(coins, m, n-coins[m])
        deletethis = self.count(coins, m+1, n)
        # if havethis:
        #     if havethis < deletethis:
        #         print coins[m], n
        #         return havethis + 1
        #     else:
        #         return deletethis + 1
        # else:
        #     if deletethis:
        #         return deletethis + 1
        #     else:
        #         return 0
        if havethis:
            if deletethis:
                if havethis < deletethis:
                    return havethis + 1
                else:
                    return deletethis
            else:
                return havethis + 1
        elif deletethis:
            return deletethis
        else:
            return 0




    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # coins = sorted(coins, reverse=True)
        # print coins
        # # num = len(coins)
        # # for i in xrange(len(coins)):
        # #     result = self.useCoin(coins[i:], amount, 0)
        # #     if result != -1:
        # #         return result
        # # return -1
        # result = self.count(coins, 0, amount)
        # if result:
        #     return result - 1
        # else:
        #     return -1


        INF = 0x7ffffffe
        dp = [0] + [INF] * amount 
        for i in xrange(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i+coin] = min(dp[i+coin],dp[i] + 1)
        return dp[amount] if dp[amount] != INF else -1






so = Solution()
print so.coinChange([186,419,83,408], 6249)
# print so.coinChange([1,3], 4)
print so.coinChange([3,7,405,436], 8839)