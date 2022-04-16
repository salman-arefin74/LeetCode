public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        List<bool> candieList = new List<bool>();
			int len = candies.GetLength(0);
			int maxValue = candies.Max();
			for(int i=0; i<len; i++)
            {
				if (candies[i] + extraCandies >= maxValue)
					candieList.Add(true);
				else
					candieList.Add(false);
            }
			return candieList;
    }
}