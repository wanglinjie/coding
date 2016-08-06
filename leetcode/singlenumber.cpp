#include <iostream>
#include <vector>
using namespace std;

/*
Given an array of integers, 
every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?


思路：
因为除了一个数字，其它数字都出现两次。
数字的二进制位进行异或操作，如果两个位相同则为0
所以将数组中每个数字进行异或操作，出现两次的数字都会等于0
最后剩余的数字就是出现一次的数字
*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        if (nums.size() <= 0)
            return 0;
        int ret = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            ret ^= nums[i];
        }
        return ret;
    }
};


int main()
{
    return 0;
}