#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n):
            if nums[i] != nums[ans]:
                ans += 1
                nums[ans] = nums[i]
        return ans + 1
# @lc code=end
