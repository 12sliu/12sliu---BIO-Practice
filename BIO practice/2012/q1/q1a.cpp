#include <iostream>
#include <sstream>
#include <string>
#include <string>
#include <sstream>
#include <cmath>
#include <stdexcept>


bool isPrime(int num){
    num = (double) num;
    for (int i = 2; i < std::pow(num, 1.0/2.0); i++){
        if (typeid(num / i) != typeid(double)) {
            return false;
        }
    }
    return true
}

int main(){
    int n;
    std::cin >> n;
    if (isPrime(n) == true){
        std::cout << n;
    } else {
        for (int i = 2; i < std::pow(n, 1.0/2.0); i++){
        
        }
    }
}