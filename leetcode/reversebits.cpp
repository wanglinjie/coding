#include <iostream>
using namespace std;
typedef unsigned int uint32_t;
/*
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
*/
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ret = 0;
        // n判断首位
        uint32_t mask = (1<<31);
        //cout<<mask<<endl;
        int bit = 1;
        for (int i = 0; i < 32; ++i)
        {
            if (n & mask)
            {
                // n首位为1，则对应位应该为1
                ret |= bit;
            }
            // 记录当前判断第几位
            bit <<= 1;
            n <<= 1;
        }
        return ret;
    }
};

int main()
{
    uint32_t n = 2;
    Solution so;
    uint32_t ret;
    ret = so.reverseBits(n);
    cout<<ret<<endl;
    return 0;
}