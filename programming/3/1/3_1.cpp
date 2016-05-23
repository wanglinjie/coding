#include <iostream>
#include <string.h>
using namespace std;
bool hasstr()
{

}
int main()
{
    char src[] = "AABBCD";
    char des[] = "CDAA";

    int len = strlen(src);
    char *newstr = new char[2 *len];
    strcpy(newstr, src);
    strcpy(newstr + len, src);
    /*for (int i = 0; i < len; i++)
    {
        char tempchar = src[0];
        for ( int j = 0; j < len - 1; j++)
            src[j] = src[j + 1];
        src[len - 1] = tempchar;
        
        if (strstr(src, des) != NULL)
        {
            cout<<"Yes! "<<src<<endl;
            return 0;
        }
    }*/
    if (strstr(newstr, des) != NULL)
    {
        cout<<"Yes"<<endl;
        return 0;
    }
    cout<<newstr<<endl;
    cout<<"No!"<<endl;
    return 0;
}