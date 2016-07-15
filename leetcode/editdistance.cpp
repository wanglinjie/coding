/*
* date:20160714
Given two words word1 and word2, 
find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
*/

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int word1Size = word1.size();
        int word2Size = word2.size();
        int m = word1Size + 1;
        int n = word2Size + 1;
        int **matrix;
        matrix = new int*[m];
        int i = 0;
        for(i = 0; i < m; i++)
        {
            matrix[i] = new int[n];
        }

        // 第一列初始化为0, 1, 2 ...
        for (i = 0; i < m; i++)
            matrix[i][0] = i;
        
        // 第一行初始化为0, 1, 2 ...
        for (i = 0; i < n; i++)
            matrix[0][i] = i;
        for (i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                int temp = 0;
                // 如果word1中第i-1为和word2中第j-1为不相等，则temp为1
                if (word1[i-1] != word2[j-1])
                    temp = 1;
                // 当前位置数值为左侧+1，右侧+1以及左上方+temp中三个值的最小值
                matrix[i][j] = min(min(matrix[i-1][j] + 1, matrix[i][j-1] + 1), matrix[i-1][j-1] + temp);
            }
        }
        int ret = matrix[m-1][n-1];
        for(i = 0; i < m; i++)
        {
            delete [] matrix[i];
        }
        delete [] matrix;
        return ret;
    }
};

int main()
{
    string word1 = "he";
    string word2 = "helle";
    Solution so;
    cout<<so.minDistance(word1, word2)<<endl;
    return 0;
}