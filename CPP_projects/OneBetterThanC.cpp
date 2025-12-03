#include <iostream>
#include<string>
#include<bitset>
using namespace std;

//function to check hex or decimal
string parse_input()
{
    string input;
        cout<<"Enter a number that is either decimal or hexadecimal: ";
        cin>>input;
        return input;
    }

// Function to check input
bool is_hex(const string input) {
    if (input.size()>2 &(input[0]=='0')&&(input[1] == 'x' // input[1]=='x')){}
}