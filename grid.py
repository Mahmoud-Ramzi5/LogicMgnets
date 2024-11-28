class Grid:
    def __init__(self, level):
        self.prev = None
        self.cols = level["cols"]
        self.rows = level["rows"]
        self.arr = [["_" for _ in range(self.cols)] for _ in range(self.rows)]
        if (
            len(level["pos_red"])
            + len(level["pos_purple"])
            + len(level["pos_grey"])
            + len(level["pos_white"])
            > self.rows * self.cols
        ):
            print("Invalid input")
            return

        for i in range(self.rows):
            for j in range(self.cols):
                if self.arr[i][j] == "_":
                    if (i, j) in level["pos_red"]:
                        self.arr[i][j] = Cell("🔴")
                    elif (i, j) in level["pos_purple"]:
                        self.arr[i][j] = Cell("🟣")
                    elif (i, j) in level["pos_grey"]:
                        self.arr[i][j] = Cell("⚫")
                    elif (i, j) in level["pos_white"]:
                        self.arr[i][j] = Cell("⚪")
                    else:
                        self.arr[i][j] = Cell("🟤")
                else:
                    if (i, j) in level["pos_red"]:
                        self.arr[i][j].setCurrVal("🔴")
                    elif (i, j) in level["pos_purple"]:
                        self.arr[i][j].setCurrVal("🟣")
                    elif (i, j) in level["pos_grey"]:
                        self.arr[i][j].setCurrVal("⚫")
                    elif (i, j) in level["pos_white"]:
                        self.arr[i][j].setCurrVal("⚪")
                    else:
                        self.arr[i][j].setCurrVal("🟤")

    def __eq__(self, other):
        if type(self) == type(other):
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.arr[i][j].currVal != other.arr[i][j].currVal:
                        return False
            return True
        else:
            return False

    def __str__(self):
        matrix = "\n"
        matrix += "   "
        for col in range(self.cols):
            matrix += f" {col + 1}  "
        matrix += "\n"
        for i in range(self.rows):
            matrix += f"{i + 1} "
            for col in self.arr[i]:
                matrix += f" {col.currVal} "
            matrix += "\n"
        return matrix

    def inGrid(self, x, y):
        if x >= 0 and x < self.rows and y >= 0 and y < self.cols:
            return True
        else:
            return False

    def checkRed(self, x, y):
        if self.arr[x][y].currVal == "🔴":
            return True
        else:
            return False

    def checkPurple(self, x, y):
        if self.arr[x][y].currVal == "🟣":
            return True
        else:
            return False

    def checkGrey(self, x, y):
        if self.arr[x][y].currVal == "⚫":
            return True
        else:
            return False

    def checkWhite(self, x, y):
        if self.arr[x][y].currVal == "⚪":
            return True
        else:
            return False

    def checkEmpty(self, x, y):
        if self.arr[x][y].currVal == "🟤":
            return True
        else:
            return False


class Cell:
    def __init__(self, val):
        self.currVal = val
        if val == "⚪":
            self.initVal = val
        else:
            self.initVal = "🟤"

    def __str__(self):
        return self.currVal

    def getCurrVal(self):
        return self.currVal

    def setCurrVal(self, val):
        self.currVal = val
