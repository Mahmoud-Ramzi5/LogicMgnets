from copy import deepcopy
from grid import Grid
from algo import Algo


class Game:
    def __init__(self, level):
        self.level = level
        self.moves = level["moves"]
        self.states = []
        self.logic = GameLogic()
        self.grid = Grid(level)
        self.algo = Algo(self.logic)
        self.algo.BFS(self.grid)
        # print(self.grid)
        # self.run()

    def run(self):
        win = False
        while self.moves:
            try:
                x, y = (
                    input("Enter source coordinates as: x,y  ex: 1,0\n")
                    .strip()
                    .split(",")
                )
                source = (int(x.strip()) - 1, int(y.strip()) - 1)
                if self.logic.checkSource(self.grid, source):
                    x, y = (
                        input("Enter destination coordinates as: x,y  ex: 0,1\n")
                        .strip()
                        .split(",")
                    )
                    dest = (int(x.strip()) - 1, int(y.strip()) - 1)
                    if self.logic.checkDestination(self.grid, dest):
                        self.states.append(deepcopy(self.grid))
                        self.logic.moveCell(source, dest)
                        print(self.grid)
                        if self.logic.checkWin(self.grid):
                            print("You Win")
                            win = True
                            break
                    else:
                        print(self.grid)
                        print("Invalid destination")
                        continue
                else:
                    print(self.grid)
                    print("Invalid source")
                    continue
            except ValueError:
                print("Invalid Input")

        if not win and self.moves == 0:
            print("You Loose")


class GameLogic:
    def checkSource(self, grid, source):
        if grid.inGrid(source[0], source[1]) and (
            grid.checkRed(source[0], source[1])
            or grid.checkPurple(source[0], source[1])
        ):
            return True
        else:
            return False

    def checkDestination(self, grid, dest):
        if grid.inGrid(dest[0], dest[1]) and (
            grid.checkWhite(dest[0], dest[1]) or grid.checkEmpty(dest[0], dest[1])
        ):
            return True
        else:
            return False

    def checkWin(self, grid):
        for i in range(grid.rows):
            for j in range(grid.cols):
                if (
                    grid.arr[i][j].initVal == "⚪" and grid.arr[i][j].currVal == "⚪"
                ) or (grid.arr[i][j].initVal == "⚪" and grid.arr[i][j].currVal == "🟤"):
                    return False
        return True

    def moveCell(self, grid, source, dest):
        source_val = grid.arr[source[0]][source[1]].getCurrVal()
        grid.arr[dest[0]][dest[1]].setCurrVal(source_val)
        grid.arr[source[0]][source[1]].setCurrVal(
            grid.arr[source[0]][source[1]].initVal
        )
        if source_val == "🔴":
            self.Pull(grid, dest)
        else:
            self.Push(grid, dest)

    def Push(self, grid, dest):
        self.pushLeftCells(grid, dest, (dest[0], dest[1] - 1))
        self.pushRightCells(grid, dest, (dest[0], dest[1] + 1))
        self.pushTopCells(grid, dest, (dest[0] - 1, dest[1]))
        self.pushBottomCells(grid, dest, (dest[0] + 1, dest[1]))

    def Pull(self, grid, dest):
        self.pullCells(grid, dest, (dest[0], dest[1] - 1))
        self.pullCells(grid, dest, (dest[0], dest[1] + 1))
        self.pullCells(grid, dest, (dest[0] - 1, dest[1]))
        self.pullCells(grid, dest, (dest[0] + 1, dest[1]))

    def pushRightCells(self, grid, rootCell, currCell):
        if not grid.inGrid(currCell[0], currCell[1]):
            return

        # Push right cells
        if (
            grid.inGrid(currCell[0], currCell[1] + 1)
            and (
                (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "🟤")
                and (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "⚪")
            )
            and (
                (grid.arr[currCell[0]][currCell[1] + 1].getCurrVal() == "🟤")
                or (grid.arr[currCell[0]][currCell[1] + 1].getCurrVal() == "⚪")
            )
        ):
            grid.arr[currCell[0]][currCell[1] + 1].setCurrVal(
                grid.arr[currCell[0]][currCell[1]].getCurrVal()
            )
            grid.arr[currCell[0]][currCell[1]].setCurrVal(
                grid.arr[currCell[0]][currCell[1]].initVal
            )
            return
        self.pushRightCells(grid, rootCell, (currCell[0], currCell[1] + 1))

    def pushLeftCells(self, grid, rootCell, currCell):
        if not grid.inGrid(currCell[0], currCell[1]):
            return

        # Push left cells
        if (
            grid.inGrid(currCell[0], currCell[1] - 1)
            and (
                (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "🟤")
                and (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "⚪")
            )
            and (
                (grid.arr[currCell[0]][currCell[1] - 1].getCurrVal() == "🟤")
                or (grid.arr[currCell[0]][currCell[1] - 1].getCurrVal() == "⚪")
            )
        ):
            grid.arr[currCell[0]][currCell[1] - 1].setCurrVal(
                grid.arr[currCell[0]][currCell[1]].getCurrVal()
            )
            grid.arr[currCell[0]][currCell[1]].setCurrVal(
                grid.arr[currCell[0]][currCell[1]].initVal
            )
            return
        self.pushLeftCells(grid, rootCell, (currCell[0], currCell[1] - 1))

    def pushTopCells(self, grid, rootCell, currCell):
        if not grid.inGrid(currCell[0], currCell[1]):
            return

        # Push top cells
        if (
            grid.inGrid(currCell[0] - 1, currCell[1])
            and (
                (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "🟤")
                and (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "⚪")
            )
            and (
                (grid.arr[currCell[0] - 1][currCell[1]].getCurrVal() == "🟤")
                or (grid.arr[currCell[0] - 1][currCell[1]].getCurrVal() == "⚪")
            )
        ):
            grid.arr[currCell[0] - 1][currCell[1]].setCurrVal(
                grid.arr[currCell[0]][currCell[1]].getCurrVal()
            )
            grid.arr[currCell[0]][currCell[1]].setCurrVal(
                grid.arr[currCell[0]][currCell[1]].initVal
            )
            return
        self.pushTopCells(grid, rootCell, (currCell[0] - 1, currCell[1]))

    def pushBottomCells(self, grid, rootCell, currCell):
        if not grid.inGrid(currCell[0], currCell[1]):
            return

        # Push bottom cells
        if (
            grid.inGrid(currCell[0] + 1, currCell[1])
            and (
                (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "🟤")
                and (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "⚪")
            )
            and (
                (grid.arr[currCell[0] + 1][currCell[1]].getCurrVal() == "🟤")
                or (grid.arr[currCell[0] + 1][currCell[1]].getCurrVal() == "⚪")
            )
        ):
            grid.arr[currCell[0] + 1][currCell[1]].setCurrVal(
                grid.arr[currCell[0]][currCell[1]].getCurrVal()
            )
            grid.arr[currCell[0]][currCell[1]].setCurrVal(
                grid.arr[currCell[0]][currCell[1]].initVal
            )
            return
        self.pushBottomCells(grid, rootCell, (currCell[0] + 1, currCell[1]))

    def pullCells(self, grid, rootCell, currCell):
        if not grid.inGrid(currCell[0], currCell[1]):
            return

        # Pull right cells
        if currCell[0] == rootCell[0] and currCell[1] > rootCell[1]:
            if (
                rootCell[1] != currCell[1] - 1
                and (
                    (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "🟤")
                    and (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "⚪")
                )
                and (
                    (grid.arr[currCell[0]][currCell[1] - 1].getCurrVal() == "🟤")
                    or (grid.arr[currCell[0]][currCell[1] - 1].getCurrVal() == "⚪")
                )
            ):
                grid.arr[currCell[0]][currCell[1] - 1].setCurrVal(
                    grid.arr[currCell[0]][currCell[1]].getCurrVal()
                )
                grid.arr[currCell[0]][currCell[1]].setCurrVal(
                    grid.arr[currCell[0]][currCell[1]].initVal
                )
            self.pullCells(grid, rootCell, (currCell[0], currCell[1] + 1))

        # Pull left cells
        if currCell[0] == rootCell[0] and currCell[1] < rootCell[1]:
            if (
                rootCell[1] != currCell[1] + 1
                and (
                    (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "🟤")
                    and (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "⚪")
                )
                and (
                    (grid.arr[currCell[0]][currCell[1] + 1].getCurrVal() == "🟤")
                    or (grid.arr[currCell[0]][currCell[1] + 1].getCurrVal() == "⚪")
                )
            ):
                grid.arr[currCell[0]][currCell[1] + 1].setCurrVal(
                    grid.arr[currCell[0]][currCell[1]].getCurrVal()
                )
                grid.arr[currCell[0]][currCell[1]].setCurrVal(
                    grid.arr[currCell[0]][currCell[1]].initVal
                )
            self.pullCells(grid, rootCell, (currCell[0], currCell[1] - 1))

        # Pull top cells
        if currCell[0] < rootCell[0] and currCell[1] == rootCell[1]:
            if (
                rootCell[0] != currCell[0] + 1
                and (
                    (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "🟤")
                    and (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "⚪")
                )
                and (
                    (grid.arr[currCell[0] + 1][currCell[1]].getCurrVal() == "🟤")
                    or (grid.arr[currCell[0] + 1][currCell[1]].getCurrVal() == "⚪")
                )
            ):
                grid.arr[currCell[0] + 1][currCell[1]].setCurrVal(
                    grid.arr[currCell[0]][currCell[1]].getCurrVal()
                )
                grid.arr[currCell[0]][currCell[1]].setCurrVal(
                    grid.arr[currCell[0]][currCell[1]].initVal
                )
            self.pullCells(grid, rootCell, (currCell[0] - 1, currCell[1]))

        # Pull bottom cells
        if currCell[0] > rootCell[0] and currCell[1] == rootCell[1]:
            if (
                rootCell[0] != currCell[0] - 1
                and (
                    (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "🟤")
                    and (grid.arr[currCell[0]][currCell[1]].getCurrVal() != "⚪")
                )
                and (
                    (grid.arr[currCell[0] - 1][currCell[1]].getCurrVal() == "🟤")
                    or (grid.arr[currCell[0] - 1][currCell[1]].getCurrVal() == "⚪")
                )
            ):
                grid.arr[currCell[0] - 1][currCell[1]].setCurrVal(
                    grid.arr[currCell[0]][currCell[1]].getCurrVal()
                )
                grid.arr[currCell[0]][currCell[1]].setCurrVal(
                    grid.arr[currCell[0]][currCell[1]].initVal
                )
            self.pullCells(grid, rootCell, (currCell[0] + 1, currCell[1]))
