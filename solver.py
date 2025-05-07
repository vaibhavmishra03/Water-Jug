from collections import deque
import heapq

class WaterJugSolver:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target

    def is_goal(self, state):
        return self.target in state

    def get_next_states(self, state):
        x, y = state
        j1, j2 = self.jug1_capacity, self.jug2_capacity
        next_states = set()

        # Fill jug1 or jug2
        next_states.add((j1, y))
        next_states.add((x, j2))

        # Empty jug1 or jug2
        next_states.add((0, y))
        next_states.add((x, 0))

        # Pour jug1 → jug2
        pour = min(x, j2 - y)
        next_states.add((x - pour, y + pour))

        # Pour jug2 → jug1
        pour = min(y, j1 - x)
        next_states.add((x + pour, y - pour))

        return next_states

    def bfs(self):
        queue = deque([((0, 0), [])])
        visited = set()

        while queue:
            (state, path) = queue.popleft()
            if state in visited:
                continue
            visited.add(state)
            new_path = path + [state]
            if self.is_goal(state):
                return new_path
            for next_state in self.get_next_states(state):
                if next_state not in visited:
                    queue.append((next_state, new_path))
        return []

    def dfs(self):
        stack = [((0, 0), [])]
        visited = set()

        while stack:
            (state, path) = stack.pop()
            if state in visited:
                continue
            visited.add(state)
            new_path = path + [state]
            if self.is_goal(state):
                return new_path
            for next_state in self.get_next_states(state):
                if next_state not in visited:
                    stack.append((next_state, new_path))
        return []

    def a_star(self):
        def heuristic(state):
            return abs(self.target - state[0]) + abs(self.target - state[1])

        open_list = [(heuristic((0, 0)), 0, (0, 0), [])]
        visited = set()

        while open_list:
            _, cost, state, path = heapq.heappop(open_list)
            if state in visited:
                continue
            visited.add(state)
            new_path = path + [state]
            if self.is_goal(state):
                return new_path
            for next_state in self.get_next_states(state):
                if next_state not in visited:
                    g = cost + 1
                    h = heuristic(next_state)
                    heapq.heappush(open_list, (g + h, g, next_state, new_path))
        return []
