class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # one pointer for the iterarion and another for the non zero elements
        positive_ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[positive_ptr] = nums[positive_ptr], nums[i]
                positive_ptr += 1


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    Solution().moveZeroes(arr)
    print(arr)
