#include <iostream>
using namespace std;

class Solution {
public:
    int hammingWeight(unsigned int n) {
        int ret = 0;
        while (n)
        {
            ret++;
            /* 对于1101000和(1101000-1)可以将第一个1消除
            所以每次n &= (n-1);可以除去1个1
            */
            n &= (n-1);
        }
        return ret;
    }
};

int main()
{
    unsigned int n;
    cin>>n;
    Solution so;
    int result = so.hammingWeight(n);
    cout<<result<<endl;
    return 0;
}