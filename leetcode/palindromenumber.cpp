#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        int y = 0;
        int temp = x;
        while (temp > 0)
        {
            y = y * 10 + temp % 10;
            temp /= 10;
        }
        if (y == x)
            return true;
        else
            return false;
    }
};

int main()
{
    return 0;
}