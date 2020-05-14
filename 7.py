class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count_element = 0
        for num in arr:
            if (num + 1) in arr:
                count_element += 1
        return count_element


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(Solution().countElements(arr))
    arr = [1, 1, 3, 3, 5, 5, 7, 7]
    print(Solution().countElements(arr))
    arr = [1, 3, 2, 3, 5, 0]
    print(Solution().countElements(arr))
    arr = [1, 1, 2, 2]
    print(Solution().countElements(arr))
