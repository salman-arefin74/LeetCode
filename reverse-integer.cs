public class Solution 
{
    public int Reverse(int x) 
    {
        int reversed = 0;
        int y = x;
        int backup = x;
        
        while(y != 0)
        {
            backup = y;
            reversed = reversed*10 + y%10;
            y = y/10;
        }
        
        if(backup != reversed % 10)
            return 0;
        
        return reversed;
    }
    
}