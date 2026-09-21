class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()
        max_area = 0

        def traverse(r, c):
            if not (
                0 <= r < num_rows
                and 0 <= c < num_cols
                and grid[r][c] == 1
                and (r, c) not in visited
            ):
                return 0

            visited.add((r, c))
            area = 1
            area += traverse(r - 1, c)
            area += traverse(r + 1, c)
            area += traverse(r, c - 1)
            area += traverse(r, c + 1)

            return area

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = traverse(r, c)
                    max_area = max(area, max_area)

        return max_area
