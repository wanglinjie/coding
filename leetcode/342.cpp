#include <iostream>
using namespace std;

/*
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
*/

class Solution {
public:
    bool isPowerOfFour(int num) {
        int i = 1;
        // 注意移位超过32位整数大小时溢出情况
        while ((i > 0) && (i <= num))
        {
            if(i == num)
                return true;
            i <<= 2;
        }
        return false;
    }
};


int main()
{
    int num;
    num = 1162261466;
    int result;
    Solution so;
    result = so.isPowerOfFour(num);

}