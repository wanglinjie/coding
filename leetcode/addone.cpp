#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> plucOne(vector<int> &digits) {
        vector<int> res(digits.size(), 0);
        int sum = 0;
        int one = 1;
        for (int i = digits.size() - 1; i >= 0; i--) {
            sum = one + digits[i];
            one = sum / 10;
            res[i] = sum % 10;
        }
        if (one > 0) {
            res.insert(res.begin(), one);
        }
        return res;
    }
};

/*
def plueOne(digits):
    one = 1
    sum = 0
    for i in xrange(len(digits)-1, -1, -1):
        sum = one + digits[i]
        one = sum / 10
        digits[i] = sum % 10
    if one > 0:
    digits.insert(0, one)
    return digits
*/

int main()
{
    cout<<"hello world!"<<endl;
    return 0;
}