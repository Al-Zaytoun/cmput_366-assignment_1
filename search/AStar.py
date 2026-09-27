from search.algorithms import State
import heapq

class AStar:

    def __init__(self, map):
        self.map = map
        self.closed = {}
        
    def search(self, start, goal):
        open = [] # A min-heap is a priority queue under-the-hood
        self.closed = {}

        start.set_cost(0)
        start.set_parent(None)
        start.set_g(0)
        solution_cost = 0
        solution_path = []
        solution_extended = 0

        heapq.heappush(open, start)

        # Main loop
        while open:
            current_node = heapq.heappop(open)
            current_node_hash = State.state_hash(current_node)

            if current_node_hash in self.closed:
                continue

            self.closed[current_node_hash] = current_node
            solution_extended += 1

            if current_node == goal:
                solution_cost = current_node.get_g()

                # get the solution_path
                curr = current_node
                while curr is not None:
                    solution_path.append(curr)
                    curr = curr.get_parent()
                solution_path.reverse()
                return solution_path, solution_cost, solution_extended
            
            neighbouring_nodes = self.map.successors(current_node)

            for neighbour_node in neighbouring_nodes:
                neighbour_node_hash = State.state_hash(neighbour_node)
                if neighbour_node_hash in self.closed:
                    continue

                neighbour_node.set_parent(current_node)

                # Calculating the heuristic of the node
                dx = abs(neighbour_node.get_x() - goal.get_x())
                dy = abs(neighbour_node.get_y() - goal.get_y())

                # 1.5 * min(dx, dy) -> refers to the diagonal moves
                # abs(dx - dy) -> refers to the cardinal moves
                heuristic_value = 1.5 * (min(dx, dy)) + abs(dx - dy)
                
                neighbour_node.set_cost(neighbour_node.get_g() + heuristic_value)
                heapq.heappush(open, neighbour_node)
        
        return None, -1, solution_extended

    def get_closed_data(self):
        return self.closed