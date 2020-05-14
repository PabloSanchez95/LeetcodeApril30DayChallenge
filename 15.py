from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)

        res = [1]

        for i in range(1, arr_len):
            prod = res[i - 1] * nums[i - 1]
            res.append(prod)

        most_right = 1
        for i in range(arr_len - 2, -1, -1):
            most_right *= nums[i + 1]
            res[i] *= most_right
        return res


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    print(Solution().productExceptSelf(arr1))
