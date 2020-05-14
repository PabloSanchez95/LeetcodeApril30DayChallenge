from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good_index_position = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_good_index_position:
                last_good_index_position = i

        return last_good_index_position == 0


if __name__ == "__main__":

    arr = [2, 3, 1, 1, 4]
    res = Solution().canJump(arr)
    print(res)
