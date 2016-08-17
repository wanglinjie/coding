#include <iostream>
using namespace std;

/*
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

从两个数字最高位开始判断相应位是否相等
记录相应位是否相等情况
从高位往低位遍历，记录开始第一个相应位不相同的位置，这个位置以及位置以后的元素应该为0
*/

class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        /*int ret = m;
        for (int i=m+1; i <= n; ++i)
            ret &= i;
        return ret;*/
        cout<<"m "<<m<<" n "<<n<<endl;
        int ret  = 0;
        ret = m & n;
        if (ret == 0)
            return ret;
        int low = m;
        int high = n;
        int bits[32];
        int j = 0;
        // 初始化记录相应位为1
        for(int i = 0; i < 32; ++i)
            bits[i] = 1;
        
        while (low != 0)
        {
            // 判断相应位是否相等
            if ((low & 0x1) != (high & 0x1))
                bits[j] = 0;
            j++;
            low >>= 1;
            high >>= 1;
        }
        if (high != 0)
        {
            // 如果high的1的最高位比low的高，则结果为0
            cout<<"high is not equal to 0"<<endl;
            return 0;
        }
        cout<<"j "<<j<<endl;
        ret = m;
        for(j = 31; j >= 0; --j) 
        {
            // 寻找两个数字第一次出现不相同的位置
            if (bits[j] == 0)
                break;
        }
        cout<<"two j "<<j<<endl;
        if (j > 0)
        {
            // 不相同位置以及以后的位置元素置0
            ret >>= j;
            ret <<= j;
        }
        return ret;
    }
};

int main()
{
    int m;
    int n;
    cin>>m>>n;
    Solution so;
    cout<<so.rangeBitwiseAnd(m, n)<<endl;
    return 0;
}