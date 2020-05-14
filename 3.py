class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = float("-inf")
        current_sum = 0
        for i in nums:
            current_sum += i
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum


if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(Solution().maxSubArray([-2]))
    print(Solution().maxSubArray([-2, -1]))
