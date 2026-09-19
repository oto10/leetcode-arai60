class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= num_rows or j >= num_cols:
                return

            if grid[i][j] == "0" or (i, j) in visited:
                return

            visited.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num_islands += 1
                    dfs(i, j)

        return num_islands
