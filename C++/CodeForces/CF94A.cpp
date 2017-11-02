#include <stdio.h>
#include <string>
#include <unordered_map>
//#include <iostream>
using namespace std;
//Compiler version g++ 6.3.0

 int main()
 {
 	string s(80,'x');
 	scanf("%s", s.begin());
 	unordered_map<string,int> dict;
 	string t(10,'x');
 	for (int i=0;i<10;++i) {
 		scanf("%s", t.begin());
 		dict.insert(pair<string,int>(t,i));
 	}
 	for (int i=0;i<8;++i) {
 		printf("%d",dict[s.substr(i*10,10)]);
 	}
 	return 0;
 }