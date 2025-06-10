from src.grid.node import Node
from src.utils import reconstruct_path


def depth_first_search(grid, start_coords, goal_coords):
    start_cell = grid.get_cell(*start_coords)
    goal_cell = grid.get_cell(*goal_coords)

    time_step = 0

    stack = [Node(start_cell, g=0)]
    visited_coords = set({Node(start_cell, g=0)})

    while stack:
        current_node = stack.pop()
        current_cell = current_node.cell
        current_coords = (current_cell.x, current_cell.y)

        time_step += 1

        if current_coords == (goal_cell.x, goal_cell.y):
            path = reconstruct_path(current_node)
            total_cost = sum(grid.get_cell(x, y).compute_cost(time_step) for (x, y) in path)
            return path, total_cost, visited_coords

        if current_coords in visited_coords:
            continue
        visited_coords.add(current_coords)

        for neighbor in reversed(grid.get_neighbors(current_cell)):
            neighbor_coords = (neighbor.x, neighbor.y)
            if neighbor_coords not in visited_coords:
                stack.append(Node(cell=neighbor, parent=current_node))

    return [], float("inf"), visited_coords
