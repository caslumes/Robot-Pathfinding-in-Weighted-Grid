import random
seed = 91
random.seed(seed)

from src.algorithms.a_star import a_star
from src.algorithms.bfs import breadth_first_search
from src.algorithms.dfs import depth_first_search
from src.algorithms.greedy_best_first import greedy_best_first

from src.grid.grid import Grid
from src.utils import generate_terrain_map, print_path_with_open


terrain_types = ['W', 'G', 'M', 'T']
terrain_weights = [0.6, 0.0, 0.4, 0.0]

width = 5
height = 5

terrain_map = generate_terrain_map(width, height, terrain_types, terrain_weights, seed)

grid = Grid(terrain_map)
start = (0, 0)
goal = (3, 3)

def test_algorithms(grid, start, goal):
    algorithms = {
        "A*": a_star,
        "Greedy Best-First": greedy_best_first,
        "Breadth-First Search": breadth_first_search,
        "Depth-First Search": depth_first_search
    }

    results = {}
    for name, algo in algorithms.items():
        path, cost, opened_coords = algo(grid, start, goal)
        results[name] = {
            "path_length": len(path),
            "cost": cost,
            "nodes_opened": len(opened_coords)
        }
        print(f'{name} algorithm:')
        print_path_with_open(grid, path, opened_coords)
        print(f'Total cost: {cost:.2f}')
        print(f'Path length: {len(path)}')
        print(f'Opened {len(opened_coords)} nodes during the search.')
        print()
    
    return results


if __name__ == "__main__":
    results = test_algorithms(grid, start, goal)

    for name, data in results.items():
        print(f"{name}: Cost={data['cost']:.2f}, Open Nodes={data['nodes_opened']}")
