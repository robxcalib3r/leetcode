## https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        o_p = 1

        for i_p in range(1, len(nums)):
            if nums[i_p] != nums[i_p - 1]:
                nums[o_p] = nums[i_p]
                o_p += 1
        return o_p