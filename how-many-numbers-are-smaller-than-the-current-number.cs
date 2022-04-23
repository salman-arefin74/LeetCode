public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        int count = 0;
			int len = nums.GetLength(0);
			int[] less = new int[len];
			for(int i= 0; i<len; i++)
            {
				count = 0;
				for (int j = 0; j < len; j++)
				{
					if(i != j && nums[j] < nums[i])
                    {
						count++;
                    }
				}
				less[i] = count;
			}
			
      return less;
    }
}