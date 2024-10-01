#include <iostream>
#include <sstream>
#include <string>
#include <string>
#include <sstream>
using namespace std;

struct Time{
  int hour;
  int minute;

//   Time(int hour, int minute){
//     this->hour = hour;
//     this->minute = minute;
//   }

  string return_time_string(){
    std::ostringstream oss;
    oss << hour << ":" << minute;
    return oss.str();
  }

  void add_minute(int m){
    minute += m;
    hour += (int) minute / 24;
    minute %= 60;
    hour %= 24;
  }
};

int main() {
  int firstSpeed, secondSpeed;
  cout << "Inputs: ";
  cin >> firstSpeed >> secondSpeed; 

  firstSpeed += 60;
  secondSpeed += 60;

  Time firstTime, secondTime;

  while (firstTime.return_time_string() != secondTime.return_time_string()){
    firstTime.add_minute(firstSpeed);
    secondTime.add_minute(secondSpeed);
    cout << firstTime.return_time_string() << " " << secondTime.return_time_string();
    break;
  }

  cout << firstTime.return_time_string();

//   cout << "Hello World!" << firstSpeed << " " << secondSpeed;
  return 0;
}

// #include <iostream>
// #include <sstream>
// #include <string>
// using std::istringstream;
// using std::string;
// using std::cout;
 
// // Driver Code
// int main()
// {
//     // Input string
//     string a("1 2 3");
 
//     // Object class of istringstream
//     istringstream my_stream(a);
 
//     // Variable to store number n
//     int n;
 
//     // Testing to see if the stream was
//     // successful and printing results.
//     while (my_stream) {
 
//         // Streaming until space is
//         // encountered
//         my_stream >> n;
 
//         // If my_stream is not empty
//         if (my_stream) {
//             cout << "That stream was successful: "
//                  << n << "\n";
//         }
 
//         // Else print not successful
//         else {
//             cout << "That stream was NOT successful!"
//                  << "\n";
//         }
//     }
 
//     return 0;
// }
