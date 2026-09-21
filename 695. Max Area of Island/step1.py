class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        island_id = 2
        max_area = 0

        def traverse(r, c, island_id):
            if not (
                0 <= r < num_rows
                and 0 <= c < num_cols
                and grid[r][c] == 1
            ):
                return

            grid[r][c] = island_id
            traverse(r - 1, c, island_id)
            traverse(r + 1, c, island_id)
            traverse(r, c - 1, island_id)
            traverse(r, c + 1, island_id)

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    traverse(r, c, island_id)
                    island_id += 1

        for id in range(2, island_id):
            area = sum(r.count(id) for r in grid)
            max_area = max(area, max_area)

        return max_area
