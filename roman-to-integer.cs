public class Solution
	{
		public int RomanToInt(string s)
		{
			int len = s.Length;
			int val = 0;
			bool flag = false;

			for (int i = 0; i < len; i++)
			{
				if (s[i].ToString().ToLower() == "i")
					val = val + 1;
				if (s[i].ToString().ToLower() == "v")
					val = val + 5;
				if (s[i].ToString().ToLower() == "x")
					val = val + 10;
				if (s[i].ToString().ToLower() == "l")
					val = val + 50;
				if (s[i].ToString().ToLower() == "c")
					val = val + 100;
				if (s[i].ToString().ToLower() == "d")
					val = val + 500;
				if (s[i].ToString().ToLower() == "m")
					val = val + 1000;
				if (i > 0)
				{
					if (s[i].ToString().ToLower() == "v" && s[i - 1].ToString().ToLower() == "i")
						val = val - 2;
					if (s[i].ToString().ToLower() == "x" && s[i - 1].ToString().ToLower() == "i")
						val = val - 2;
					if (s[i].ToString().ToLower() == "l" && s[i - 1].ToString().ToLower() == "x")
						val = val - 20;
					if (s[i].ToString().ToLower() == "c" && s[i - 1].ToString().ToLower() == "x")
						val = val - 20;
					if (s[i].ToString().ToLower() == "d" && s[i - 1].ToString().ToLower() == "c")
						val = val - 200;
					if (s[i].ToString().ToLower() == "m" && s[i - 1].ToString().ToLower() == "c")
						val = val - 200;
				}
			}

			return val;
		}
	}