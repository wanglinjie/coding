#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <stdexcept>
#include <csignal>
#include <unistd.h>

using namespace std;

#define PI 3.1415926
#define MIN(a,b) (((a)<(b))?a:b)

#define concat(a, b) a ## b
template <class T>
class Stack {
private:
    vector<T> elems;

public:
    void push(T const&);
    void pop();
    T top() const;
    bool empty() const {
        return elems.empty();
    }
};

template <class T>
void Stack<T>::push (T const& elem)
{
    elems.push_back(elem);
}

template <class T>
void Stack<T>::pop()
{
    if (elems.empty())
    {
        throw out_of_range("Stack<>::pop():empty stack");
    }
    elems.pop_back();
}

template <class T>
T Stack<T>::top() const
{
    if (elems.empty())
    {
        throw out_of_range("Stack<>::top():empty stack");
    }

    return elems.back();
}

void signalHandler(int signum)
{
    cout<<"Interrupt signal ("<<signum<<") received."<<endl;
    exit(signum);
}

int main()
{
    /*try {
        Stack<int> intStack;
        Stack<string> stringStack;

        intStack.push(7);
        cout<<intStack.top()<<endl;

        stringStack.push("hello");
        cout<<stringStack.top()<<endl;
        stringStack.pop();
        // stringStack.pop();
    }
    catch (exception const& ex)
    {
        cout<<"Exception: "<<ex.what()<<endl;
        return -1;
    }
    cout<<PI<<endl;
    cout<<MIN(3, 5)<<endl;
    int xy = 100;
    cout<<concat(x, y)<<endl;
    cout<<__LINE__<<endl;*/
    signal(SIGINT, signalHandler);
    while(1)
    {
        cout<<"Going to sleep..."<<endl;
        sleep(1);
    }
    return 0;
}