class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = set()

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        def dfs(r, c, index):

            # 1. Are we still in the Grid border?
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # 2. Current word of Cell is needable for now?
            if board[r][c] != word[index]:
                return False

            # 3. Is this cell used for this path?
            if (r, c) in visited:
                return False

            # 4. Use current path
            visited.add((r, c))

            # 5. Did we find the last word?
            if index == len(word) - 1:
                visited.remove((r, c))
                return True

            # 6. Check all of the possibilities
            found = False

            for dr, dc in directions:
                next_r = r + dr
                next_c = c + dc

                if dfs(next_r, next_c, index + 1):
                    found = True
                    break

            visited.remove((r, c))

            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False