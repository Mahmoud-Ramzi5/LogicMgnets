from copy import deepcopy


class Algo:
    def __init__(self, Logic):
        self.logic = Logic
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
