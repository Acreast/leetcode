// Last updated: 7/12/2025, 11:47:26 PM
class Solution {
public:
     int numberOfWays(string corridor) {
        int mod = pow(10,9) + 7;
        long long ans = 1;
        int temp = 0;
        int count = 0;
        for(int i = 0; i < corridor.length(); i++){
            if(count != 2){
                if(corridor[i]=='S'){
                    count++;
                }
            }
            else{
                if(corridor[i]=='S'){
                    temp++;
                    ans *= temp;
                    ans %= mod;
                    count = 1;
                    temp = 0;
                }
                else{
                    temp++;
                }
            }

        }
        if(count != 2){
            return 0;
        }
        else{
            return ans;
        }
    }
};