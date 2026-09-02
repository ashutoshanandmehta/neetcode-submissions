class Solution {
public:
    bool solve(const vector<int>& nums, int target) {
        vector<bool> dp(target + 1, false);
        dp[0] = true;

        for (int num : nums) {
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }

    bool canPartition(vector<int>& nums) {
        int sum = 0;

        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
        }

        if (sum % 2 != 0) {
            return false;
        }

        return solve(nums, sum / 2);
    }
};