#include <iostream>
#include <vector>
using namespace std;

/*
date:20160729
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prices_num = prices.size();
        if (prices_num == 0)
            return 0;
        int max_profit = 0;
        for (int i = 1; i < prices_num; i++)
        {
            // 判断当前位置值是否比前一个值大，如果大则可以获得利润
            if (prices[i] > prices[i-1])
                max_profit += (prices[i] - prices[i-1]);
        }
        return max_profit;
    }
};

int main()
{
    return 0;
}