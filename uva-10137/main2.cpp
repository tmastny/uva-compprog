#include <cstdio>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
typedef long long int lli;
typedef vector<lli> vi;
typedef vector<vi> vvi;
typedef vector<float> vf;

int main(){
 	double n;

 	while(cin >> n, n){
  		cin.ignore();
  		vi prices;
  		lli total = 0;
  		for(int i=0;i<n;i++){
   			int a,b;
   			scanf("%d.%d",&a,&b);
   			total += a*100+b;
   			prices.push_back(a*100+b);
  		}

  		double mean = (double)total/n;
  	  	lli ans = 0;
  	  	lli ans_ = 0;
  	  	for(int i=0;i<n;i++){
   	   		// spend - desired_spend
          lli a = prices[i]-mean;
   	   		double b =prices[i]-mean;
   	   		if(a>0){
    			ans += a;
   	   		} else {
    			ans_ += a;
   	   		}
  	  	}
  	  	ans_ = -ans_;
  	  	double ansf = ans >= ans_ ? ans:ans_;
  	  	printf("$%.2f\n",ansf/100.0);
 	}
	return 0;
}
