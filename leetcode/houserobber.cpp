#include <iostream>
#include <vector>
using namespace std;

/*
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing 
each of them is that adjacent houses have security system connected 
and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

思路：
使用一个额外的vector存储到当前位置最好的收益
遍历每户人家，ret当前位置存储到达当前最好的收益
ret[i] = max(ret[i-1], max(ret[i-2]+nums[i-2], nums[i-2]));
一直到i户人家，收益最大的情况可能是到达i-1收益最大
也可能是i-2以及以前收益加上当前收益，或者是仅仅当前这户人家收益
*/

class Solution {
public:
    int rob(vector<int>& nums) {
        int size = nums.size();
        if (size <= 0)
            return 0;
        
        vector<int> ret(size+2, 0);
        for(int i = 2; i < size+2; ++i)
        {
            // 获取到i户人家，最大收益
            ret[i] = max(ret[i-1], max(ret[i-2]+nums[i-2], nums[i-2]));
        }
        // 返回遍历到最后一户人家最大收益
        return ret[size+1];
    }
};

int main()
{
    int n[] = {1, 2, 3, 4, 5};
    vector<int> nums(n, n+5);
    Solution so;
    int ret;
    ret = so.rob(nums);
    cout<<ret<<endl;
    return 0;
}