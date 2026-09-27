from search.map import Map
from search.algorithms import State
import heapq

class Dijkstra:

    def __init__(self, map):
        self.map = map
        self.closed = {}


    def search(self, start, goal):

        open = [] #  (Min heap data type) Nodes we have seen, but have not yet finalized the decision
        self.closed = {} # (state_hash, state object) -> Nodes we have finalized on (had the shortest distance)

        solution_path = []
        solution_cost = 0
        solution_extended = 0

        start.set_g(0)
        start.set_cost(0)
        start.set_parent(None)

        heapq.heappush(open, start)

        while open:
            current_node = heapq.heappop(open)
            current_hash = State.state_hash(current_node)

            if current_hash in self.closed:
                continue
            else:
                self.closed[current_hash] = current_node
                solution_extended += 1

                if current_node == goal:
                    solution_cost = current_node.get_g()
                    
                    # Calculate solution path
                    path_node = current_node
                    while path_node is not None:
                        solution_path.append(path_node)
                        path_node = path_node.get_parent()

                    solution_path.reverse()
                    return solution_path, solution_cost, solution_extended
                
                neighbouring_nodes = self.map.successors(current_node)
                for neighbour_node in neighbouring_nodes:
                    neighbour_node_hash = neighbour_node.state_hash()
                    neighbour_node.set_parent(current_node)
                    neighbour_node.set_cost(neighbour_node.get_g())

                    if neighbour_node_hash in self.closed:
                        continue
                    else:
                        heapq.heappush(open, neighbour_node)



        return None, -1, solution_extended

    def get_closed_data(self):
        return self.closed

        