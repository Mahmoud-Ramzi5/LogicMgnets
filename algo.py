from copy import deepcopy


class Algo:
    def __init__(self, Logic):
        self.logic = Logic
        self.visited = []
        self.queue = []

    def BFS(self, grid):
        self.visited.append(deepcopy(grid))

        # TODO check win
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
