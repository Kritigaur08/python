class Solution:
    """
        A class to find if a path exists from the top left corner of a matrix to the bottom right corner.
    """

    def isValid(self, row, col, m, n, vis, grid) -> bool:
        """
                Checks if the given cell is valid.

                Args:
                    row: The row index of the cell.
                    col: The column index of the cell.
                    m: The number of rows in the matrix.
                    n: The number of columns in the matrix.
                    vis: The visited cells.
                    grid: The matrix.

                Returns:
                    True if the cell is valid, False otherwise.
        """
        if row < 0 or col < 0 or row >= m or col >= n:
            return False
        if grid[row][col] == 0:
            return False
        if vis[row][col] == True:
            return False
        return True

    def pathExist(self, row, col, grid: list[list[int]]) -> bool:
        """
                Finds if a path exists from the top left corner of the matrix to the bottom right corner.

                Args:
                    row: The row index of the current cell.
                    col: The column index of the current cell.
                    grid: The matrix.

                Returns:
                    True if a path exists, False otherwise.
        """
        m = len(grid[0])
        n = len(grid)
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]

        vis = [[False for i in range(m)] for j in range(n)]

        st = []
        st.append([row, col])

        while len(st) > 0:
            curr = st[len(st) - 1]
            st.remove(st[len(st) - 1])
            row = curr[0]
            col = curr[1]

            if self.isValid(row, col, m, n, vis, grid) == False:
                continue

            vis[row][col] = True

            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                st.append([adjx, adjy])

            if row == 4 and col == 4:
                return True
        return False


if __name__ == "__main__":
    p = Solution()
    matrix = [[1, 0, 0, 0, 1],
              [1, 1, 0, 0, 1],
              [1, 1, 1, 0, 1],
              [1, 1, 1, 1, 0],
              [1, 0, 0, 1, 1]]

    matrix2 = [[1, 0, 0, 0, 1],
               [1, 1, 0, 0, 1],
               [1, 1, 1, 0, 1],
               [1, 1, 1, 0, 0],
               [1, 0, 0, 1, 1]]

    print(p.pathExist(0, 0, matrix))
    print(p.pathExist(0, 0, matrix2))
