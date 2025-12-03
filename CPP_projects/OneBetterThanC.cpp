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
    if (input.size()>2&&(input[0]=='0')&&(input[1] == 'x' ||input[1]=='X')){
        return true;
    }
    return false;
}   
// Function for converting to binary
string to_binary(const string input){
    unsigned int number;
    
    if (is_hex(input)){
        number = stoul(input, nullptr,16);
    }else{
        number = stoul(input, nullptr,10);
    }
    // converting to binary using bitset
    bitset<32>binary(number);
    return binary.to_string();
}
// connecting the functions
int main() {
    string input = parse_input();
    cout<<"Binary: "<<to_binary(input)<<endl;
    return 0;
}