#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prices_size = prices.size();
        if (prices_size == 0)
            return 0;
        int max_profit = 0;
        int min_value_left = prices[0];
        for (int i = 1; i < prices_size; i++)
        {
            if (prices[i] > min_value_left)
            {
                int value = prices[i] - min_value_left;
                if (value > max_profit)
                    max_profit = value;
            }
            else
            {
                min_value_left = prices[i];
            }
        }
        return max_profit;
        
    }
};

int main()
{
    return 0;
}