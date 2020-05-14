class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)

        prev = [0] * (N2 + 1)
        now = [0] * (N2 + 1)

        best = 0

        for x in range(1, N1 + 1):
            for y in range(1, N2 + 1):
                if text1[x - 1] == text2[y - 1]:
                    now[y] = max(prev[y - 1] + 1, now[y])
                now[y] = max(prev[y], now[y])
                now[y] = max(now[y - 1], now[y])
                best = max(best, now[y])
            for y in range(len(prev)):
                prev[y] = now[y]
                now[y] = 0

        return best
