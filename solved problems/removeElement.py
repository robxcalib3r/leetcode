## https://leetcode.com/submissions/detail/1333777066/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        o_p = 0
        for i_p in range(len(nums)):
            if nums[i_p] != val:
                nums[o_p] = nums[i_p]
                o_p += 1
        return o_p
        