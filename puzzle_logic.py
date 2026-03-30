import random

class PuzzleLogic:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.goal_state = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]
        self.goal_state[rows-1][cols-1] = 0
        
        self.goal_positions = {
            self.goal_state[i][j]: (i, j)
            for i in range(self.rows)
            for j in range(self.cols)
        }

    def generate_default_state(self):
        state = [[i * self.cols + j + 1 for j in range(self.cols)] for i in range(self.rows)]
        state[self.rows-1][self.cols-1] = 0
        flat_state = [item for row in state for item in row]
        while True:
            random.shuffle(flat_state)
            if self.is_solvable(flat_state):
                break
        return [list(flat_state[i*self.cols:(i+1)*self.cols]) for i in range(self.rows)]

    def is_solvable(self, flat_state):
        inversions = 0
        arr = [x for x in flat_state if x != 0]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    inversions += 1
        if self.cols % 2 == 1:
            return inversions % 2 == 0
        else:
            blank_row_from_bottom = self.rows - (flat_state.index(0) // self.cols)
            return (inversions + blank_row_from_bottom) % 2 == 0

    def position(self, state):
        return tuple(item for row in state for item in row)

    def tuple_to_state(self, tup):
        return [list(tup[i*self.cols:(i+1)*self.cols]) for i in range(self.rows)]

    def get_neighbors(self, state):
        neighbors = []
        x, y = next((i, j) for i in range(self.rows) for j in range(self.cols) if state[i][j] == 0)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)
        return neighbors

    def heuristic(self, state):
        return sum(abs(i - self.goal_positions[v][0]) + abs(j - self.goal_positions[v][1])
                   for i in range(self.rows) for j in range(self.cols) if (v:=state[i][j]) != 0)
