#include <iostream>
#include <vector>
using namespace std;


/*
Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

从2开始往n遍历，如果当前数组存储数字不为0，则当前是素数
将素数的倍数位置值置为0，表示不是素数
*/
class Solution {
public:
    int countPrimes(int n) {
        int ret = 0;
        if (n <= 1)
            return ret;
        vector<int> num(n, 0);
        // 初始化
        for(int i = 0; i < n; i++)
            num[i] = i;
        for(int i = 2; i < n; i++)
        {
            // 从2往n遍历


            if(num[i] != 0)
            {
                // 当前元素值不为0，则是素数
                ret++;
                int j = num[i] * 2;

                // 将素数的倍数置为0
                while (j < n)
                {
                    num[j] = 0;
                    j += num[i];
                }
            }
        }
        return ret;
        
    }
};

int main()
{
    int n;
    cin>>n;
    Solution so;
    result = so.countPrimes(n);
    cout<<result<<endl;
    return 0;
}