from search.map import Map
from search.algorithms import State
import heapq

class Dijkstra:

    def __init__(self, map):
        self.map = Map


    def search(self, start, goal):
        start = State()
        goal = State()

        open = []
        closed = []

        start.set_g(0)
        start.set_cost(0)
        start.set_parent(0)

        heapq.heappush(open, start)
        while open:
            current_node = heapq.heappop()
    