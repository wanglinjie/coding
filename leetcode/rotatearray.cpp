#include <iostream>
#include <vector>
using namespace std;

/*
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

思路：
可以将整个数组调换顺序，然后将前k个调换顺序，后面的调换顺序
*/
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int size = nums.size();
        if (size <= 1 || k <= 0)
            return;
        k %= size;
        // 将整个数组反序，使得后面k个数字可以在数字前面
        rotate(nums, 0, size-1);
        // 前k个数字反序
        rotate(nums, 0, k-1);
        // 剩余数字反序
        rotate(nums, k, size-1);
        
    }
    void rotate(vector<int>& nums, int start, int end)
    {
        if (start >= end)
            return;
        int temp;
        while (start < end)
        {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
};

int main()
{
    int n[] = {1, 2, 3, 4, 5};
    vector<int> nums(n, n+5);
    Solution so;
    so.rotate(nums, 0);
    for (int i = 0; i < nums.size(); ++i)
    {
        cout<<nums[i]<<" ";
    }
    cout<<endl;
    return 0;
}