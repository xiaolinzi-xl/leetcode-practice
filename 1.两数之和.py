#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# 思路：使用哈希表存储元素和位置
# 时间复杂度：O(n)

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            if target - nums[i] in record:
                return [record[target-nums[i]], i]
            else:
                record[nums[i]] = i
# @lc code=end
