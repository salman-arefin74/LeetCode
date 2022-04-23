public class Solution {
    public int NumJewelsInStones(string J, string S) {
        int total = 0;
			int len = J.Length;
			string one = "";
			string two = "";
			for (int i = 0; i < len; i++)
			{
				one = J.Substring(i, 1);
				for(int j=0; j< S.Length; j++)
                {
					two = S.Substring(j, 1);
					if (one == two)
						total++;
                }
			}
      
			return total;
    }
}