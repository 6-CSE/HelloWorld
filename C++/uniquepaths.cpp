class Solution {
public:
    int solve(int i, int j, vector<vector<int>> &dp, int& m, int& n) {
        if(i == m-1 || j == n-1) return 1;
        if(dp[i][j] != 0)return dp[i][j];
        
        dp[i][j] = solve(i+1, j, dp, m, n) + solve(i, j+1, dp, m, n);
        return dp[i][j];
    }
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m , vector<int>(n , 0));
        return solve(0, 0, dp, m, n);
    }
};
