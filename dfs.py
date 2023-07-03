class Solution:
    """
    A class to implement the Depth First Search algorithm.
    """

    def isValid(self, row, col, m, n, vis):
        """
        Check if the given row and column indices are valid.

        Args:
            row: The row index.
            col: The column index.
            m: The number of rows in the grid.
            n: The number of columns in the grid.
            vis: The visited array.

        Returns:
            True if the indices are valid, False otherwise.
        """

        if row < 0 or col < 0 or row >= m or col >= n:
            return False
        if vis[row][col] == True:
            return False
        return True

    def dfs(self, row, col, grid: list[list[int]]):
        """
        Perform a Depth First Search on the given grid.

        Args:
            row: The starting row index.
            col: The starting column index.
            grid: The grid.
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

            # Check if the current cell is valid
            if self.isValid(row, col, m, n, vis) == False:
                continue

            # Print the value of the current cell
            print(grid[row][col], end=" ")

            # Mark the current cell as visited
            vis[row][col] = True

            # Add the four adjacent cells to the stack
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                st.append([adjx, adjy])


if __name__ == "__main__":
    """
    Main function.
    """

    p = Solution()
    grid = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]
    p.dfs(0, 0, grid)