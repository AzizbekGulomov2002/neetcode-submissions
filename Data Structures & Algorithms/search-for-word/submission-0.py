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

            # 1. Grid chegarasidan chiqib ketdikmi?
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # 2. Hozirgi cell'dagi harf kerakli harfmi?
            if board[r][c] != word[index]:
                return False

            # 3. Bu cell oldin shu path'da ishlatilganmi?
            if (r, c) in visited:
                return False

            # 4. Hozirgi cell'dan foydalanamiz
            visited.add((r, c))

            # 5. So'zning oxirgi harfini ham topdikmi?
            if index == len(word) - 1:
                visited.remove((r, c))
                return True

            # 6. To'rtta yo'nalishni tekshiramiz
            found = False

            for dr, dc in directions:
                next_r = r + dr
                next_c = c + dc

                if dfs(next_r, next_c, index + 1):
                    found = True
                    break

            # 7. Shu cell'dan foydalanish tugadi
            visited.remove((r, c))

            return found

        # 8. Har bir cell'dan boshlashga harakat qilamiz
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == word[0]:

                    if dfs(r, c, 0):
                        return True

        return False