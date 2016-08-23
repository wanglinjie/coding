#include <iostream>
using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int s1_len = s1.size();
        int s2_len = s2.size();
        int s3_len = s3.size();
        if ((s1_len + s2_len) != s3_len)
            return false;
        if (s1_len == 0)
            return s2 == s3;
        if (s2_len == 0)
            return s1 == s3;
        bool s1_result = false;
        bool s2_result = false;
        if (s1[0] == s3[0])
            s1_result = isInterleave(s1.substr(1, s1_len-1), s2, s3.substr(1, s3_len-1));
        if (s2[0] == s3[0])
            s2_result = isInterleave(s1, s2.substr(1, s2_len-1), s3.substr(1, s3_len-1));
        return s1_result || s2_result;
    }
};

int main()
{
    string s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb";
    string s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc";
    string s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc";
    Solution so;
    bool result = so.isInterleave(s1, s2, s3);
    cout<<result<<endl;
    return 0;
}