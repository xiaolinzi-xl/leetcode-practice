#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l,r = 1,x
        ans = -1
        while l <= r:
            mid = (l+r) // 2
            if mid ** 2 <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


    def mySqrt_1(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        mid = 1
        while mid * mid <= x:
            mid += 1
        return mid - 1

# @lc code=end

