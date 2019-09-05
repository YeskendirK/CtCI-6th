# Solution-1: Using Recursion

def robot_in_grid(maze):
    if maze is None or len(maze) == 0:
        return None
    path = []
    if get_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
        return path
    return True


def get_path(maze, row, col, path):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    at_origin = (row == 0) and (col == 0)
    if at_origin or get_path(maze, row - 1, col, path) or get_path(maze, row, col - 1, path):
        point = (row, col)
        path.append(point)
        return True

    return False


# Solution-2: Memoized

def robot_in_grid_memo(maze):
    if maze is None or len(maze) == 0:
        return None
    path = []
    failed_points = []
    if get_path_memo(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return True


def get_path_memo(maze, row, col, path, failed_points):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    point = (row, col)
    if point in failed_points:
        return False

    at_origin = (row == 0) and (col == 0)
    if at_origin or get_path_memo(maze, row - 1, col, path, failed_points) or get_path_memo(maze, row, col - 1, path,
                                                                                            failed_points):
        path.append(point)
        return True

    failed_points.append(point)
    return False
