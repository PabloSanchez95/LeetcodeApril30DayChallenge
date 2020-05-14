class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_hash = {}

        for num in nums:
            if num in nums_hash:
                nums_hash[num] += 1
            else:
                nums_hash[num] = 1

        for key in nums_hash:
            if nums_hash[key] == 1:
                return key

    def singlenumberbit(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a


if __name__ == "__main__":
    arr = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(arr))
    print(Solution().singlenumberbit(arr))
