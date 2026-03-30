import heapq
from collections import deque
import time

class PuzzleSolver:
    def __init__(self, logic, gui_callback=None, check_stop_flag=None):
        self.logic = logic
        self.gui_callback = gui_callback
        self.check_stop_flag = check_stop_flag
        self.generated_nodes = 0
        self.visited_nodes = 0

    def _update_gui(self):
        if self.gui_callback and self.visited_nodes % 500 == 0:
            self.gui_callback()

    def _is_stopped(self):
        if self.check_stop_flag:
            return self.check_stop_flag()
        return False

    def reset_stats(self):
        self.generated_nodes = 0
        self.visited_nodes = 0

    def bfs_solve(self, start_state, goal_state):
        self.reset_stats()
        start = self.logic.position(start_state)
        goal = self.logic.position(goal_state)
        if start == goal: return []
        
        queue, visited = deque([(start, [])]), {start}
        while queue:
            if self._is_stopped(): return None
            self._update_gui()
            
            current, path = queue.popleft()
            self.visited_nodes += 1
            
            for neighbor in self.logic.get_neighbors(self.logic.tuple_to_state(current)):
                self.generated_nodes += 1
                neighbor_tup = self.logic.position(neighbor)
                if neighbor_tup not in visited:
                    if neighbor_tup == goal: return path + [neighbor]
                    queue.append((neighbor_tup, path+[neighbor]))
                    visited.add(neighbor_tup)
        return None

    def dfs_solve(self, start_state, goal_state, limit=30):
        self.reset_stats()
        start = self.logic.position(start_state)
        goal = self.logic.position(goal_state)
        if start == goal: return []

        stack, visited = [(start, [], 0)], {start: 0}

        while stack:
            if self._is_stopped(): return None
            self._update_gui()

            current, path, depth = stack.pop()
            self.visited_nodes += 1

            if current == goal:
                return path

            if depth < limit:
                for neighbor in self.logic.get_neighbors(self.logic.tuple_to_state(current)):
                    self.generated_nodes += 1
                    neighbor_tup = self.logic.position(neighbor)
                    if neighbor_tup not in visited or depth + 1 < visited[neighbor_tup]:
                        stack.append((neighbor_tup, path+[neighbor], depth+1))
                        visited[neighbor_tup] = depth + 1
        return None

    def iddfs_solve(self, start_state, goal_state, start_limit=100, max_limit=500):
        self.reset_stats()
        for limit in range(start_limit, max_limit + 1):
            if self._is_stopped(): return None, limit
            self._update_gui()
            
            path = self.dfs_solve(start_state, goal_state, limit=limit)
            if path:
                return path, limit
            if self._is_stopped(): return None, limit
        return None, max_limit

    def ucs_solve(self, start_state, goal_state):
        self.reset_stats()
        start = self.logic.position(start_state)
        goal = self.logic.position(goal_state)
        
        pq, visited = [(0, start, [])], {start: 0}
        while pq:
            if self._is_stopped(): return None
            self._update_gui()
            
            cost, current, path = heapq.heappop(pq)
            self.visited_nodes += 1
            if current == goal: return path
            
            for neighbor in self.logic.get_neighbors(self.logic.tuple_to_state(current)):
                self.generated_nodes += 1
                neighbor_tup = self.logic.position(neighbor)
                new_cost = cost + 1
                if neighbor_tup not in visited or new_cost < visited[neighbor_tup]:
                    visited[neighbor_tup] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor_tup, path+[neighbor]))
        return None

    def astar_solve(self, start_state, goal_state):
        self.reset_stats()
        start = self.logic.position(start_state)
        goal = self.logic.position(goal_state)
        
        pq, visited = [(self.logic.heuristic(start_state), 0, start, [])], {start: 0}
        while pq:
            if self._is_stopped(): return None
            self._update_gui()
            
            f, g, current, path = heapq.heappop(pq)
            self.visited_nodes += 1
            if current == goal: return path
            
            for neighbor in self.logic.get_neighbors(self.logic.tuple_to_state(current)):
                self.generated_nodes += 1
                neighbor_tup = self.logic.position(neighbor)
                new_g, new_f = g+1, g+1+self.logic.heuristic(neighbor)
                if neighbor_tup not in visited or new_g < visited[neighbor_tup]:
                    visited[neighbor_tup] = new_g
                    heapq.heappush(pq, (new_f, new_g, neighbor_tup, path+[neighbor]))
        return None

    def greedy_solve(self, start_state, goal_state):
        self.reset_stats()
        start = self.logic.position(start_state)
        goal = self.logic.position(goal_state)
        
        pq, visited = [(self.logic.heuristic(start_state), start, [])], {start}
        while pq:
            if self._is_stopped(): return None
            self._update_gui()
            
            h, current, path = heapq.heappop(pq)
            self.visited_nodes += 1
            if current == goal:
                return path
                
            for neighbor in self.logic.get_neighbors(self.logic.tuple_to_state(current)):
                self.generated_nodes += 1
                neighbor_tup = self.logic.position(neighbor)
                if neighbor_tup not in visited:
                    visited.add(neighbor_tup)
                    heapq.heappush(pq, (self.logic.heuristic(neighbor), neighbor_tup, path+[neighbor]))
        return None

    def beam_solve(self, start_state, goal_state, beam_width=3):
        self.reset_stats()
        start = self.logic.position(start_state)
        goal = self.logic.position(goal_state)
        if start == goal: return []

        frontier = [(self.logic.heuristic(start_state), start, [])]  
        visited = set([start])

        while frontier:
            if self._is_stopped(): return None
            self._update_gui()
            
            new_frontier = []
            for _, current, path in frontier:
                self.visited_nodes += 1
                if current == goal:
                    return path
                for neighbor in self.logic.get_neighbors(self.logic.tuple_to_state(current)):
                    self.generated_nodes += 1
                    neighbor_tup = self.logic.position(neighbor)
                    if neighbor_tup not in visited:
                        visited.add(neighbor_tup)
                        new_frontier.append((self.logic.heuristic(neighbor), neighbor_tup, path+[neighbor]))
            if not new_frontier:
                break
            frontier = heapq.nsmallest(beam_width, new_frontier, key=lambda x: x[0])
        return None
