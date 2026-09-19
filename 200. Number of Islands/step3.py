class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        visited = set()

        def traverse(r, c):
            if not (
                0 <= r < num_rows
                and 0 <= c < num_cols
                and (r, c) not in visited
                and grid[r][c] == "1"
            ):
                return

            visited.add((r, c))
            traverse(r - 1, c)
            traverse(r + 1, c)
            traverse(r, c - 1)
            traverse(r, c + 1)

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_islands += 1
                    traverse(r, c)

        return num_islands
