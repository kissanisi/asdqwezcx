#include <iostream>

using namespace std;

int main() {
  string a = "test", b = "@!#$",res="";
  for(int i = 0; i<4; i++){
     res+=(char)(a[i]^b[i]);
  }
  cout << res;
  return 0;
}
