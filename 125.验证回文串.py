#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        l, r = 0, len(s) - 1
        val_s = s.lower()
        validate_s = set('0123456789qwertyuiopasdfghjklzxcvbnm')
        while l < r:
            if val_s[l] not in validate_s:
                l += 1
            elif val_s[r] not in validate_s:
                r -= 1
            elif val_s[l] != val_s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
# @lc code=end
