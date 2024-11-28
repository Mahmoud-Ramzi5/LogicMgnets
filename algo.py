from copy import deepcopy


class Algo:
    def __init__(self, Logic, level):
        self.logic = Logic
        self.level = level
        self.visited = []
        self.queue = []
        self.stack = []

    def construct_path(self, grid):
        path = []
        curr = grid
        while curr != None:
            path.append(curr)
            curr = curr.prev
        path.reverse()
        return path

    def BFS(self, grid):
        self.queue = []
        self.visited = []
        self.queue.append(grid)

        while len(self.queue) > 0:
            board = self.queue.pop(0)
            self.visited.append(board)

            # check win
            if self.logic.checkWin(board):
                print("BFS WON, Path: ->", end="")
                for p in self.construct_path(board):
                    print(p, end="")
                print()
                return True

            for i in range(board.rows):
                for j in range(board.cols):
                    if (
                        board.arr[i][j].currVal == "🟣"
                        or board.arr[i][j].currVal == "🔴"
                    ):
                        for k in range(board.rows):
                            for l in range(board.cols):
                                temp = deepcopy(board)
                                temp.prev = board
                                if (
                                    temp.arr[k][l].currVal == "⚪"
                                    or temp.arr[k][l].currVal == "🟤"
                                ):
                                    self.logic.moveCell(temp, (i, j), (k, l))
                                    if temp not in self.visited:
                                        self.queue.append(temp)
        return False

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
            print("DFS WON, Path: ->", end="")
            for p in self.construct_path(grid):
                print(p, end="")
            print()
            return True

        for i in range(grid.rows):
            for j in range(grid.cols):
                if grid.arr[i][j].currVal == "🟣" or grid.arr[i][j].currVal == "🔴":
                    for k in range(grid.rows):
                        for l in range(grid.cols):
                            temp = deepcopy(grid)
                            temp.prev = grid
                            if (
                                temp.arr[k][l].currVal == "⚪"
                                or temp.arr[k][l].currVal == "🟤"
                            ):
                                self.logic.moveCell(temp, (i, j), (k, l))
                                if temp not in self.visited:
                                    if self.DFS(temp):
                                        return True
        return False

    def DFS_moves(self, grid, moves):
        self.visited.append((grid, moves))

        # check win
        if self.logic.checkWin(grid):
            print("DFS With Moves WON, Path: ->", end="")
            for p in self.construct_path(grid):
                print(p, end="")
            print()
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
                            temp.prev = grid
                            if (
                                temp.arr[k][l].currVal == "⚪"
                                or temp.arr[k][l].currVal == "🟤"
                            ):
                                self.logic.moveCell(temp, (i, j), (k, l))
                                if (temp, moves) not in self.visited:
                                    if self.DFS_moves(temp, moves - 1):
                                        return True
        return False

    def g_cost(self, current_moves):
        return current_moves + 1

    def UCS(self, grid, current_moves):
        self.queue = []
        self.visited = []
        self.queue.append((current_moves, grid))

        while len(self.queue) > 0:
            board = self.queue.pop(0)
            self.visited.append(board)

            for i in range(board[1].rows):
                for j in range(board[1].cols):
                    if (
                        board[1].arr[i][j].currVal == "🟣"
                        or board[1].arr[i][j].currVal == "🔴"
                    ):
                        for k in range(board[1].rows):
                            for l in range(board[1].cols):
                                temp = deepcopy(board[1])
                                temp.prev = board[1]
                                if (
                                    temp.arr[k][l].currVal == "⚪"
                                    or temp.arr[k][l].currVal == "🟤"
                                ):
                                    self.logic.moveCell(temp, (i, j), (k, l))

                                    move_cost = self.g_cost(current_moves)
                                    total_moves = current_moves + move_cost

                                    # check win
                                    if self.logic.checkWin(temp):
                                        print("UCS WON, Path: ->", end="")
                                        for p in self.construct_path(temp):
                                            print(p, end="")
                                        print()
                                        return True

                                    if (total_moves, temp) not in self.visited:
                                        self.queue.append((total_moves, temp))
                                        self.queue.sort(key=lambda q: q[0])
        return False

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
                                temp.prev = grid
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
                print("Hill Climb Got this, Path: ->", end="")
                for p in self.construct_path(best_grid):
                    print(p, end="")
                print(f"min cost got: {min_cost}")
                return True

            min_cost = best[0]
            best_grid = best[1]
            grid = best[1]

            neighbors = []
        return None

    def A_star(self, grid, current_moves):
        self.queue = []
        self.visited = []
        h_cost = self.hurestic(grid, self.level["pos_white"])
        g_cost = current_moves
        total_cost = h_cost + g_cost
        self.queue.append((total_cost, grid))

        while len(self.queue) > 0:
            board = self.queue.pop(0)
            self.visited.append(board)

            # check win
            if self.logic.checkWin(board[1]):
                print("A* WON, Path: ->", end="")
                for p in self.construct_path(board[1]):
                    print(p, end="")
                print()
                return True

            for i in range(board[1].rows):
                for j in range(board[1].cols):
                    if (
                        board[1].arr[i][j].currVal == "🟣"
                        or board[1].arr[i][j].currVal == "🔴"
                    ):
                        for k in range(board[1].rows):
                            for l in range(board[1].cols):
                                temp = deepcopy(board[1])
                                temp.prev = board[1]
                                if (
                                    temp.arr[k][l].currVal == "⚪"
                                    or temp.arr[k][l].currVal == "🟤"
                                ):
                                    self.logic.moveCell(temp, (i, j), (k, l))

                                    h_new = self.hurestic(temp, self.level["pos_white"])
                                    move_cost = self.g_cost(current_moves)
                                    new_cost = h_new + move_cost

                                    if (new_cost, temp) not in self.visited:
                                        self.queue.append((new_cost, temp))
                                        self.queue.sort(key=lambda q: q[0])
        return False
