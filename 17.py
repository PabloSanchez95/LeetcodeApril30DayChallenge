from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        no_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    no_islands += 1
                    self.getSurrounding(grid, i, j)

        return no_islands

    def getSurrounding(self, grid: List[List[int]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.getSurrounding(grid, i - 1, j)  # arriba
        self.getSurrounding(grid, i + 1, j)  # abajo
        self.getSurrounding(grid, i, j - 1)  # izquierda
        self.getSurrounding(grid, i, j + 1)  # derecha


if __name__ == "__main__":
    islands = [
        [11110],
        [11010],
        [11000],
        [00000],
    ]
    islands = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(Solution().numIslands(islands))
