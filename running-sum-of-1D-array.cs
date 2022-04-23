public class Solution {
    public int[] RunningSum(int[] nums) {
        int sum = 0;
  			int len = nums.GetLength(0);
  			int[] nums2 = new int[len];
  			nums2[0] = nums[0];
  			sum = nums[0];
  			int i;
  			for(i=1; i<len; i++)
              {
  				sum = sum + nums[i];
  				nums2[i] = sum;
              }
  
  			return nums2;
    }
}