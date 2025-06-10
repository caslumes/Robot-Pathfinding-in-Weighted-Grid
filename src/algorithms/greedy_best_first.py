import heapq
from src.grid.node import Node
from src.heuristic import heuristic
from src.utils import reconstruct_path


def greedy_best_first(grid, start_coords, goal_coords):
    start_cell = grid.get_cell(*start_coords)
    goal_cell = grid.get_cell(*goal_coords)

    open_set = []
    heapq.heappush(open_set, Node(start_cell, g=0, h=heuristic(start_cell, goal_cell)))
    visited_coords = set()

    time_step = 0

    while open_set:
        current_node = heapq.heappop(open_set)
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

        for neighbor in grid.get_neighbors(current_cell):
            neighbor_coords = (neighbor.x, neighbor.y)
            if neighbor_coords in visited_coords:
                continue

            new_node = Node(
                cell=neighbor,
                parent=current_node,
                g=0,  # ignored
                h=heuristic(neighbor, goal_cell)
            )
            heapq.heappush(open_set, new_node)

    total_cost = sum(grid.get_cell(x, y).get_cost(0) for (x, y) in path)
    return None, float('inf'), visited_coords
