#include <iostream>
#include <sstream>
#include <string>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>

using namespace std;

// int main(){
//     vector<int> numbers = {1, 1, 2, 3, 5, 8, 13, 21, 34};
//     int target = 13;
//     while (true){
//         cout << "test";
//         int index = std::floor(numbers.size() / 2);
//         if (numbers.size() % 2 == 0) {
//             index--;
//         }
//         vector<int>::iterator start;
//         vector<int>::iterator end;
//         vector<int> result(index);
//         if (numbers.at(index) == target){
//             cout << index << "\n BROKE BROKE AA";
//             break;
//         } else if (numbers.at(index) > target){
//             start = numbers.begin();
//             end = numbers.begin() + index;
//         } else {
//             start = numbers.begin() + index+1;
//             end = numbers.end();
//         }
//         copy(start, end, result.begin());
//         for(int i : result) {
//             cout << i << "TEST\n";
//         };
//         numbers = result;
//     }
//     return 0;
// }

int main(){
    vector<int> numbers = {0, 1, 2, 3, 5, 8, 13, 21};
    int target = 1;

    int start = 0; 
    int end = numbers.size() - 1; 
    cout << "please work";
    while (true){
        int index = std::floor((start + end) / 2);
        if (numbers.at(index) == target) {
            cout << "you win! " << index;
            break; 
        } else if (numbers.at(end) == target){
            cout << "you win!" << end;
            break;
        } else if (numbers.at(index) > target) {
            end = index;
        } else {
            start = index;
        }

        // vector<int>::iterator startiter = numbers.begin() + start;
        // vector<int>::iterator enditer = numbers.begin() + end;
        // vector<int> result(end - start);
        // copy(startiter, enditer, result.begin());
        // for (int i : result){
        //     cout << i << "\n";
        // }
        // break;

    }
    return 0;
}