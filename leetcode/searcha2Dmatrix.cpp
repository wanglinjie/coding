/*
date:20160714
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
*/

#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    bool searchMatrix(vector<vector<int> >& matrix, int target) {
        
    }
};

int main()
{
    vector<int> v(10);
    for (int i = 0; i < 10; i++)
    {
        v[i] = (i+1) * ( i+1);
    }
    for (int i = 9; i > 0; i--)
    {
        v[i] -= v[i-1];
    }
    cout<<v.size()<<endl;
    if (v.empty())
    {
        cout<<"yes"<<endl;
    }
    else
        cout<<"it not empty"<<endl;
    v.push_back(10);
    cout<<v.size()<<endl;
    v.resize(25);
    cout<<v.size()<<endl;
    vector<string> names(20, "Unknown");
    cout<<names[1]<<endl;
    int N, M;
    N = 10;
    M = 10;
    vector< vector<int> > Matrix(N, vector<int>(M, -1));
    cout<<Matrix[3][3]<<endl;
    return 0;
}