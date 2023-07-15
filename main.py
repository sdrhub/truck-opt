import numpy as np
from bin_coordinates import bins

# bins = []

'''with open('bin_coordinates.py','r') as f:
    for line in f:
        x,y = line.strip().split()
        bins.append((float(x),float(y)))'''


def read_coordinates_from_file(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0].strip()
            x = float(parts[1].strip())
            y = float(parts[2].strip())
            coordinates.append((name, x, y))
    return coordinates


def calculate_distance(coord1, coord2):
    x1, y1 = map(float, coord1[1:])
    x2, y2 = map(float, coord2[1:])
    return ((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5


def calculate_total_distance(route, coordinates):
    total_distance = 0
    for i in range(len(route) - 1):
        current_coord = coordinates[int(route[i])]
        next_coord = coordinates[int(route[i + 1])]
        total_distance += calculate_distance(current_coord, next_coord)
    return total_distance


def aco_algorithm(coordinates, num_ants, num_iterations, evaporation_rate, alpha, beta):
    num_coordinates = len(coordinates)
    pheromone_matrix = np.ones((num_coordinates, num_coordinates))
    best_route = None
    best_distance = float('inf')

    for iteration in range(num_iterations):

        routes = []
        for ant in range(num_ants):
            visited = set()
            route = []
            current_node = np.random.randint(num_coordinates)
            route.append(current_node)
            visited.add(current_node)

            while len(visited) < num_coordinates:
                next_node = None
                probabilities = []

                for node in range(num_coordinates):
                    if node not in visited:
                        pheromone = pheromone_matrix[int(current_node), int(node)]
                        distance = calculate_distance(coordinates[int(current_node)], coordinates[int(node)])
                        if distance == 0:
                            probabilities.append((node, 0))
                        else:
                            probabilities.append((node, pheromone ** alpha / distance ** beta))

                probabilities = np.array(probabilities)
                probabilities[:, 1] /= np.sum(probabilities[:, 1])
                probabilities[:, 1] = np.nan_to_num(probabilities[:, 1])
                next_node = np.random.choice(probabilities[:, 0], p=probabilities[:, 1])

                route.append(next_node)
                visited.add(next_node)
                current_node = next_node

            routes.append(route)

            distance = calculate_total_distance(route, coordinates)
            for i in range(len(route) - 1):
                node1 = int(route[i])
                node2 = int(route[i + 1])
                pheromone_matrix[node1, node2] += 1 / distance

        for route in routes:
            distance = calculate_total_distance(route, coordinates)
            if distance < best_distance:
                best_distance = distance
                best_route = route

    return best_route, best_distance


num_ants = 10
num_iterations = 100
evaporation_rate = 0.5
alpha = 1
beta = 2
import numpy as np
from bin_coordinates import bins

# bins = []

'''with open('bin_coordinates.py','r') as f:
    for line in f:
        x,y = line.strip().split()
        bins.append((float(x),float(y)))'''


def read_coordinates_from_file(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0].strip()
            x = float(parts[1].strip())
            y = float(parts[2].strip())
            coordinates.append((name, x, y))
    return coordinates


def calculate_distance(coord1, coord2):
    x1, y1 = map(float, coord1[1:])
    x2, y2 = map(float, coord2[1:])
    return ((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5


def calculate_total_distance(route, coordinates):
    total_distance = 0
    for i in range(len(route) - 1):
        current_coord = coordinates[int(route[i])]
        next_coord = coordinates[int(route[i + 1])]
        total_distance += calculate_distance(current_coord, next_coord)
    return total_distance


def aco_algorithm(coordinates, num_ants, num_iterations, evaporation_rate, alpha, beta):
    num_coordinates = len(coordinates)
    pheromone_matrix = np.ones((num_coordinates, num_coordinates))
    best_route = None
    best_distance = float('inf')

    for iteration in range(num_iterations):

        routes = []
        for ant in range(num_ants):
            visited = set()
            route = []
            current_node = np.random.randint(num_coordinates)
            route.append(current_node)
            visited.add(current_node)

            while len(visited) < num_coordinates:
                next_node = None
                probabilities = []

                for node in range(num_coordinates):
                    if node not in visited:
                        pheromone = pheromone_matrix[int(current_node), int(node)]
                        distance = calculate_distance(coordinates[int(current_node)], coordinates[int(node)])
                        if distance == 0:
                            probabilities.append((node, 0))
                        else:
                            probabilities.append((node, pheromone ** alpha / distance ** beta))

                probabilities = np.array(probabilities)
                probabilities[:, 1] /= np.sum(probabilities[:, 1])
                probabilities[:, 1] = np.nan_to_num(probabilities[:, 1])
                next_node = np.random.choice(probabilities[:, 0], p=probabilities[:, 1])

                route.append(next_node)
                visited.add(next_node)
                current_node = next_node

            routes.append(route)

            distance = calculate_total_distance(route, coordinates)
            for i in range(len(route) - 1):
                node1 = int(route[i])
                node2 = int(route[i + 1])
                pheromone_matrix[node1, node2] += 1 / distance

        for route in routes:
            distance = calculate_total_distance(route, coordinates)
            if distance < best_distance:
                best_distance = distance
                best_route = route

    return best_route, best_distance


num_ants = 10
num_iterations = 100
evaporation_rate = 0.5
alpha = 1
beta = 2
