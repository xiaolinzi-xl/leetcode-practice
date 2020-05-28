#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        record = set()
        n = len(nums)
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                tmp_sum = nums[l] + nums[r]
                if tmp_sum == -nums[i]:
                    if (nums[i], nums[l], nums[r]) not in record:
                        ans.append([nums[i], nums[l], nums[r]])
                        record.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif tmp_sum > -nums[i]:
                    r -= 1
                else:
                    l += 1
        return ans

# @lc code=end
