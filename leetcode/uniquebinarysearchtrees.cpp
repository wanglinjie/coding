#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int numTrees(int n) {
        if (n <= 0)
            return 0;
        vector<int> record(n+1, 1);
        record[0] = 1;
        for (int i = 2; i <= n; i++)
        {
            int number = 0;
            for (int j = 1; j <= i; j++ )
            {
                int left = record[j-1];
                int right = record[i - j];
                int temp = 1;
                if (left == 0 || right == 0)
                    temp = left + right;
                else
                    temp = left * right;
                number += temp;
            }
            record[i] = number;
        }
        return record[n];
    }
};

int main()
{
    int n = 10;
    Solution so;
    int result = so.numTrees(n);
    cout<<result<<endl;
    return 0;
}