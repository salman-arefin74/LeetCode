public class Solution {
    public int NumIdenticalPairs(int[] nums) {
        int num = 0;
			int i, j;
			int len = nums.GetLength(0);
			for (i=0; i<len; i++)
            {
				for (j = 0; j < len; j++)
				{
					if (nums[i] == nums[j] && i < j)
						num++;
				}
			}
			return num;
    }
}