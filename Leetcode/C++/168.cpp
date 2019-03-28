class Solution {
public:
    string convertToTitle(int n) {
        string res;
        char ch;
        while(n!=0){
            ch = 'A'+ (n - 1) % 26;
            res = ch + res;
            n = (n - 1) / 26;
        }
        return res;
    }
};