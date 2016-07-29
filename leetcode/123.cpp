#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices)
    {
/*
It is similar to other buy/sell problems. 
just do DP and define an array of states to track the current maximum profits at different stages.
For example, in the below code

states[][0]: one buy，一次买
states[][1]: one buy, one sell，一次买，一次卖
states[][2]: two buys, one sell，两次买，一次卖
states[][3]: two buy, two sells，两次买，两次卖
The states transistions occurs when buy/sell operations are executed. 
For example, state[][0] can move to state[][1] via one sell operation.
*/
        int states[2][4] = {INT_MIN, 0, INT_MIN, 0};
        int len = prices.size();
        int cur = 0, next = 1;
        for (int i = 0; i < len; i++)
        {
            // 循环遍历prices中值，四种遍历四种情况
            states[next][0] = max(states[cur][0], -prices[i]);
            states[next][1] = max(states[cur][1], states[cur][0]+prices[i]);
            states[next][2] = max(states[cur][2], states[cur][1]-prices[i]);
            states[next][3] = max(states[cur][3], states[cur][2]+prices[i]);
            int temp = cur;
            cur = next;
            next = temp;
        }
        return max(states[cur][1], states[cur][3]);
    }

    int maxProfitK(vector<int> &prices)
    {

/*
// f[k, ii] represents the max profit up until prices[ii] 
(Note: NOT ending with prices[ii]) using at most k transactions. 
// f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
//          = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
// f[0, ii] = 0; 0 times transation makes 0 profit
// f[k, 0] = 0; if there is only one price data point you can't make any money no matter 
how many times you can trade
*/
        int len = prices.size();
        if (len <= 1)
            return 0;
        else
        {
            int K = 2;
            int maxProf = 0;
            vector< vector<int> > f(K+1, vector<int>(len, 0));
            for (int kk = 1; kk <= K; kk++)
            {
                int tmpMax = f[kk-1][0] - prices[0];
                for (int ii = 1; ii < len; ii++)
                {
                    f[kk][ii] = max(f[kk][ii-1], prices[ii]+tmpMax);
                    tmpMax = max(tmpMax, f[kk-1][ii] - prices[ii]);
                    maxProf = max(f[kk][ii], maxProf);
                }
            }
            return maxProf;
        }
    }

};

int main()
{
    return 0;
}