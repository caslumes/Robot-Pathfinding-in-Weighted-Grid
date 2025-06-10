from collections import deque
from src.grid.node import Node
from src.utils import print_path_with_open, reconstruct_path


def breadth_first_search(grid, start_coords, goal_coords):
    start_cell = grid.get_cell(*start_coords)

    time_step = 0

    start_node = Node(start_cell, g=0)
    queue = deque([start_node])
    visited_coords = set({start_node})

    while queue:
        current_node = queue.popleft()
        current_cell = current_node.cell
        current_coords = (current_cell.x, current_cell.y)

        time_step += 1

        if current_coords == goal_coords:
            path = reconstruct_path(current_node)
            total_cost = sum(grid.get_cell(x, y).compute_cost(time_step) for (x, y) in path)
            return path, total_cost, visited_coords

        if current_coords in visited_coords:
            continue
        visited_coords.add(current_coords)

        for neighbor in grid.get_neighbors(current_cell):
            neighbor_coords = (neighbor.x, neighbor.y)
            if neighbor_coords not in visited_coords:
                queue.append(Node(cell=neighbor, parent=current_node))

    return [], float("inf"), visited_coords
