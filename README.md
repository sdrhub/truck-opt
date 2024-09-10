Optimal Truck Route Finder Using Ant Colony Optimization (ACO)

This Python script implements an Ant Colony Optimization (ACO) algorithm to find the optimal route for a truck driver responsible for collecting bins across a mapped area. The project is based on a real map of **Kavala city** with actual bin locations. It was developed as part of a university project focused on solving real-world routing problems.

Features:
- Bin Coordinate Input**: Reads a map of bin locations from a CSV file, with each bin having a unique identifier and (x, y) coordinates.
- Route Optimization**: Calculates the shortest possible route for a truck to visit all bins based on the ACO algorithm.
- Ant Colony Optimization**: Utilizes a population of "ants" to explore different route possibilities and find the most efficient path.
- Pheromone Simulation**: Pheromone trails guide the ants towards better routes over successive iterations, simulating real-world ant behavior.
- Customizable Parameters**: Allows adjustment of the number of ants, iterations, evaporation rate, and the importance of pheromone vs. distance.

How it works:
1. The script reads a file containing the real bin coordinates for Kavala Greece.
2. Ants traverse the map, exploring different routes and depositing pheromones based on the quality (shortness) of the route.
3. Over multiple iterations, the algorithm finds the optimal or near-optimal route for the truck to follow.

Key Parameters:
- Number of Ants**: The size of the ant population.
- Number of Iterations**: The number of times the ants will explore the routes.
- Evaporation Rate**: Controls how quickly the pheromone levels decay over time.
- Alpha and Beta**: Control the influence of pheromone trails and distance, respectively.
