#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#


def moveZeroes_1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                zero_idx += 1
                nums[zero_idx] = nums[i]
        for i in range(zero_idx+1, len(nums)):
            nums[i] = 0

#TODO 优化两个loop
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                zero_idx += 1
                nums[zero_idx] = nums[i]
        for i in range(zero_idx+1, len(nums)):
            nums[i] = 0

# @lc code=end
