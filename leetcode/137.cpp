#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ret = 0;
        int mask = 1;
        for(int i = 0; i < 32; i++)
        {
            int num = 0;
            for(int j = 0; j < nums.size(); j++)
            {
                if (nums[j] & mask)
                    num++;
            }
            num %= 3;
            mask <<= 1;
            ret |= (num << i);
        }
        return ret;
    }
};


int main()
{
    return 0;
}