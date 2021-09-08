int a = nums1.size();
int b = nums2.size();
int len = 0;
std::vector<std::vector<int>> dp(a + 1, std::vector<int>(b + 1));
for (int i = 1; i <= a; ++i)
{
	for (int j = 1; j <= a; ++j)
	{
		if (nums1[i - 1] == nums2[j - 1])
		{
			dp[i][j] = dp[i - 1][j - 1] + 1;
			len = std::max(len, dp[i][j]);
		}
	}
}
return len;