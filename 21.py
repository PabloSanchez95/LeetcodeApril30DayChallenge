# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        N, M = binaryMatrix.dimensions()
        best = M
        for row in range(N):
            column = self.find(row, M, binaryMatrix)
            best = min(best, column)

        if best == M:
            return -1
        return best

    def find(self, row, M, binaryMatrix):
        left = 0
        right = M

        while left < right:
            middle = (left + right) // 2
            if binaryMatrix.get(row, middle) == 0:
                left = middle + 1
            else:
                right = middle
        return left
