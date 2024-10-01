#include <iostream>
#include <sstream>
#include <string>
#include <string>
#include <sstream>

int fibonacci(int target, int previous1, int previous2){
    int nextNum = previous1 + previous2;
    if (nextNum > target){
        return previous1;
    }
    return fibonacci(target, nextNum, previous1);
}

int main(){
    int n;
    std::cin >> n;
    while (n > 0){
        int biggestNum = fibonacci(n, 1, 1);
        n -= biggestNum;
        std::cout << biggestNum << " "; 
    }
}