import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)
        ans = 0
        running_sum = 0

        count[running_sum] = 1
        for num in nums:
            running_sum += num
            previous = running_sum - k
            if previous in count:
                ans += count[previous]
            count[running_sum] += 1

        return ans
