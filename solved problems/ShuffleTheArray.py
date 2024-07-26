class Solution(object):
    ## Normal Solution
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        temp_arr = []

        for indx in range(len(nums)-n):
            temp_arr.append(nums[indx])
            temp_arr.append(nums[indx + n])

        return temp_arr
    
    ## Faster solution in same array
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n]

        j = 2 * n - 1
        for i in range(n-1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10

            nums[j] = y
            nums[j - 1] = x
            j -= 2

        return nums


if __name__ == "__main__":
    case1 = [2,5,1,3,4,7]
    n1 = 3
    case2 = [1,2,3,4,4,3,2,1]
    n2 = 4

    sol = Solution()
    print(sol.shuffle(case1, n1))