#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def hashPath(self, maze: list, start: list, destination: list):
        # Get the number of rows and columns in the maze grid
        rows, columns = len(maze), len(maze[0])

        # Create a set to keep track of visited positions during DFS
        visited = set()

        # Define the DFS function with parameters (x, y) representing the current position
        def dfs(x, y):
            # If the current position (x, y) is already visited, return False
            if (x, y) in visited:
                return False

            # Mark the current position as visited
            visited.add((x, y))

            # If the current position is the destination point, return True
            if [x, y] == destination:
                return True

            # Define the four possible directions to move: right, left, down, and up
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            # Loop through each direction and try to explore in that direction
            for dx, dy in directions:
                nx, ny = x, y
                # Explore in a direction until we hit a wall (maze[nx+dx][ny+dy] == 1)
                while 0 <= nx + dx < rows and 0 <= ny + dy < columns and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy

                # Recursively check if we can reach the destination from the new position (nx, ny)
                if dfs(nx, ny):
                    return True

            # If no valid path is found from the current position, return False
            return False

        # Start DFS from the given start point and return the result
        return dfs(start[0], start[1])

