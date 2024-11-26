from copy import deepcopy


class Algo:
    def __init__(self, Logic, level):
        self.logic = Logic
        self.level = level
        self.visited = []
        self.queue = []
        self.stack = []

    def BFS(self, grid):
        self.visited.append(deepcopy(grid))

        # check win
        if self.logic.checkWin(grid):
            print("BFS WON")
            return

        for i in range(grid.rows):
            for j in range(grid.cols):
                if grid.arr[i][j].currVal == "🟣" or grid.arr[i][j].currVal == "🔴":
                    for k in range(grid.rows):
                        for l in range(grid.cols):
                            temp = deepcopy(grid)
                            if (
                                temp.arr[k][l].currVal == "⚪"
                                or temp.arr[k][l].currVal == "🟤"
                            ):
                                self.logic.moveCell(temp, (i, j), (k, l))
                                if temp not in self.visited:
                                    self.queue.append(temp)

        board = self.queue.pop(0)
        print(board)
        self.BFS(board)

    # def DFS(self, grid):
    #     self.visited.append(deepcopy(grid))

    #     # check win
    #     if self.logic.checkWin(grid):
    #         print("DFS WON")
    #         return

    #     for i in range(grid.rows):
    #         for j in range(grid.cols):
    #             if grid.arr[i][j].currVal == "🟣" or grid.arr[i][j].currVal == "🔴":
    #                 for k in range(grid.rows):
    #                     for l in range(grid.cols):
    #                         temp = deepcopy(grid)
    #                         if (
    #                             temp.arr[k][l].currVal == "⚪"
    #                             or temp.arr[k][l].currVal == "🟤"
    #                         ):
    #                             self.logic.moveCell(temp, (i, j), (k, l))
    #                             if temp not in self.visited:
    #                                 self.stack.append(temp)

    #     board = self.stack.pop()
    #     print(board)
    #     self.DFS(board)

    def DFS(self, grid):
        self.visited.append(deepcopy(grid))

        # check win
        if self.logic.checkWin(grid):
            print("DFS WON")
            return True

        for i in range(grid.rows):
            for j in range(grid.cols):
                if grid.arr[i][j].currVal == "🟣" or grid.arr[i][j].currVal == "🔴":
                    for k in range(grid.rows):
                        for l in range(grid.cols):
                            temp = deepcopy(grid)
                            if (
                                temp.arr[k][l].currVal == "⚪"
                                or temp.arr[k][l].currVal == "🟤"
                            ):
                                self.logic.moveCell(temp, (i, j), (k, l))
                                if temp not in self.visited:
                                    print(temp)
                                    if self.DFS(temp):
                                        return True
        return False

    def DFS_moves(self, grid, moves):
        self.visited.append((grid, moves))

        # check win
        if self.logic.checkWin(grid):
            print("DFS With Moves WON")
            return True

        if moves <= 0:
            print("Max Moves reached")
            return False

        for i in range(grid.rows):
            for j in range(grid.cols):
                if grid.arr[i][j].currVal == "🟣" or grid.arr[i][j].currVal == "🔴":
                    for k in range(grid.rows):
                        for l in range(grid.cols):
                            temp = deepcopy(grid)
                            if (
                                temp.arr[k][l].currVal == "⚪"
                                or temp.arr[k][l].currVal == "🟤"
                            ):
                                self.logic.moveCell(temp, (i, j), (k, l))
                                if (temp, moves) not in self.visited:
                                    print(temp)
                                    if self.DFS_moves(temp, moves - 1):
                                        return True
        return False

    def UCS(self, grid, moves, path):
        self.visited.append((grid, moves))

        # check win
        if self.logic.checkWin(grid):
            path.append((grid, moves))
            return True

        for i in range(grid.rows):
            for j in range(grid.cols):
                if grid.arr[i][j].currVal == "🟣" or grid.arr[i][j].currVal == "🔴":
                    for k in range(grid.rows):
                        for l in range(grid.cols):
                            temp = deepcopy(grid)
                            if (
                                temp.arr[k][l].currVal == "⚪"
                                or temp.arr[k][l].currVal == "🟤"
                            ):
                                self.logic.moveCell(temp, (i, j), (k, l))
                                if (temp, moves + 1) not in self.visited:
                                    self.queue.append((temp, moves + 1))
        return False

    def CallUCS(self, grid):
        path = []
        path.append((grid, 0))
        self.queue.append((grid, 0))

        while len(self.queue) > 0:
            board = self.queue.pop(0)

            if self.UCS(board[0], board[1] + 1, path):
                print("UCS WON")
                for state in path:
                    print(state[0])
                    print(f"move number {state[1]}")
                break

    def hurestic(self, grid, pos_white):
        cost = 0

        for i in range(grid.rows):
            for j in range(grid.cols):
                if grid.arr[i][j].currVal == "⚫":
                    min_distance = 10e10
                    for white in pos_white:
                        distance = abs(white[0] - i) + abs(white[1] - j)
                        if distance < min_distance:
                            min_distance = distance
                    cost += min_distance

                if grid.arr[i][j].currVal == "🟣" or grid.arr[i][j].currVal == "🔴":
                    if grid.arr[i][j].initVal != "⚪":
                        cost += 1

        return cost

    def hill_climb(self, initial):
        print(initial)
        min_cost = self.hurestic(initial, self.level["pos_white"])
        grid = deepcopy(initial)
        best_grid = grid
        neighbors = []

        while True:
            for i in range(grid.rows):
                for j in range(grid.cols):
                    if grid.arr[i][j].currVal == "🟣" or grid.arr[i][j].currVal == "🔴":
                        for k in range(grid.rows):
                            for l in range(grid.cols):
                                temp = deepcopy(grid)
                                if (
                                    temp.arr[k][l].currVal == "⚪"
                                    or temp.arr[k][l].currVal == "🟤"
                                ):
                                    self.logic.moveCell(temp, (i, j), (k, l))
                                    curr_cost = self.hurestic(
                                        temp, self.level["pos_white"]
                                    )
                                    neighbors.append((curr_cost, temp))

            # best neighbor
            best = min(neighbors, key=lambda neighbor: neighbor[0])

            if best[0] >= min_cost:
                return (min_cost, best_grid)

            min_cost = best[0]
            best_grid = best[1]
            grid = best[1]

            neighbors = []
        return None
