class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        offset = 0

        while m > 0 or n > 2:
            if m == n and m % 2 == 1:
                ans |= 1 << offset

            offset += 1
            m //= 2
            n //= 2
        return ans


if __name__ == "__main__":
    res = Solution().rangeBitwiseAnd(5, 7)
    res = Solution().rangeBitwiseAnd(0, 1)
    res = Solution().rangeBitwiseAnd(0, 2147483647)
    print(res)
