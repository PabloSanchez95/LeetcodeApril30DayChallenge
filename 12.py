class Solution(object):
    def lastStoneWeightRecur(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 1:
            return stones[0]

        first_max = max(stones)
        stones.remove(first_max)
        second_max = max(stones)
        stones.remove(second_max)

        if first_max != second_max:
            stones.append(first_max - second_max)
        if not stones:
            stones.append(0)
        return self.lastStoneWeight(stones)

    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            first_max = max(stones)
            stones.remove(first_max)
            second_max = max(stones)
            stones.remove(second_max)

            if first_max != second_max:
                stones.append(first_max - second_max)
        return stones[0] if stones else 0


if __name__ == "__main__":
    arr1 = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(arr1))
    arr1 = [2, 2]
    print(Solution().lastStoneWeight(arr1))
