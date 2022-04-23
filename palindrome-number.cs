public class Solution {
    public bool IsPalindrome(int x) {
        int backup = x;
        int reversed = 0;
        bool res = false;
        while(x != 0)
        {
            reversed = reversed*10 + x%10;
            x = x/10;    
        }
        if(backup < 0)
            res = false;
        else if(backup == reversed)
            res = true;
        
        return res;
    }
}