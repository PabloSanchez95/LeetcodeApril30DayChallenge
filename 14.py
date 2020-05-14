class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """

        # postive = right 1
        # negative = left 0
        final_shift = 0
        for op in shift:
            if op[0]:
                final_shift += op[1]
            else:
                final_shift -= op[1]

        final_shift = final_shift % len(s) if final_shift % len(s) > 0 else final_shift
        if final_shift > 0:
            part2 = s[: len(s) - final_shift]
            part1 = s[len(s) - final_shift : len(s)]
            s = f"{part1}{part2}"
        else:
            final_shift = abs(final_shift)
            part1 = s[final_shift + 1 : len(s)]
            part2 = s[0 : final_shift + 1]
            s = f"{part1}{part2}"

        return s


if __name__ == "__main__":
    # s = "abc"
    # shift = [[0, 1], [1, 2]]
    # print(Solution().stringShift(s, shift))
    # s = "abcdefg"
    # shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
    # print(Solution().stringShift(s, shift))
    # s = "wpdhhcj"
    # shift = [[0, 7], [1, 7], [1, 0], [1, 3], [0, 3], [0, 6], [1, 2]]
    # print(Solution().stringShift(s, shift))
    s = "xqgwkiqpif"
    shift = [
        [1, 4],
        [0, 7],
        [0, 8],
        [0, 7],
        [0, 6],
        [1, 3],
        [0, 1],
        [1, 7],
        [0, 5],
        [0, 6],
    ]
    print(Solution().stringShift(s, shift))
