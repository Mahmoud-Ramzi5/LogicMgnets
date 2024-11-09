from game import Game


class main:
    levels = [
        {  # 1
            "cols": 4,
            "rows": 3,
            "moves": 5,
            "pos_red": [],
            "pos_purple": [(2, 0)],
            "pos_grey": [(1, 2)],
            "pos_white": [(1, 1), (1, 3)],
        },
        {  # 2
            "cols": 5,
            "rows": 5,
            "moves": 5,
            "pos_red": [],
            "pos_purple": [(4, 0)],
            "pos_grey": [(1, 2), (2, 1), (2, 3), (3, 2)],
            "pos_white": [(0, 2), (2, 0), (2, 2), (2, 4), (4, 2)],
        },
        {  # 3
            "cols": 4,
            "rows": 3,
            "moves": 5,
            "pos_red": [],
            "pos_purple": [(2, 0)],
            "pos_grey": [(1, 2)],
            "pos_white": [(0, 3), (2, 3)],
        },
        {  # 4
            "cols": 3,
            "rows": 5,
            "moves": 2,
            "pos_red": [],
            "pos_purple": [(2, 0)],
            "pos_grey": [(1, 1), (3, 1)],
            "pos_white": [(0, 0), (0, 2), (4, 1)],
        },
        {  # 5
            "cols": 3,
            "rows": 4,
            "moves": 2,
            "pos_red": [],
            "pos_purple": [(3, 1)],
            "pos_grey": [(1, 0), (1, 2), (2, 0), (2, 2)],
            "pos_white": [(0, 0), (1, 0), (3, 0), (0, 2), (1, 2)],
        },
        {  # 6
            "cols": 5,
            "rows": 3,
            "moves": 2,
            "pos_red": [],
            "pos_purple": [(2, 0)],
            "pos_grey": [(1, 1), (1, 3)],
            "pos_white": [(0, 3), (1, 2), (2, 3)],
        },
        {  # 7
            "cols": 4,
            "rows": 5,
            "moves": 2,
            "pos_red": [],
            "pos_purple": [(2, 1)],
            "pos_grey": [(1, 0), (2, 0), (3, 1), (3, 2)],
            "pos_white": [(0, 0), (1, 0), (2, 3), (3, 2), (4, 3)],
        },
        {  # 8
            "cols": 4,
            "rows": 3,
            "moves": 2,
            "pos_red": [],
            "pos_purple": [(2, 0)],
            "pos_grey": [(1, 1), (1, 2)],
            "pos_white": [(0, 0), (0, 2), (2, 2)],
        },
        {  # 9
            "cols": 7,
            "rows": 1,
            "moves": 2,
            "pos_red": [],
            "pos_purple": [(0, 0)],
            "pos_grey": [(0, 3), (0, 5)],
            "pos_white": [(0, 1), (0, 3), (0, 5)],
        },
        {  # 10
            "cols": 4,
            "rows": 4,
            "moves": 2,
            "pos_red": [],
            "pos_purple": [(0, 0)],
            "pos_grey": [(2, 2), (2, 3), (3, 1)],
            "pos_white": [(1, 1), (1, 3), (3, 0), (3, 3)],
        },
        {  # 11
            "cols": 5,
            "rows": 2,
            "moves": 1,
            "pos_red": [(1, 2)],
            "pos_purple": [],
            "pos_grey": [(0, 0), (0, 4)],
            "pos_white": [(0, 1), (0, 2), (0, 3)],
        },
        {  # 12
            "cols": 4,
            "rows": 5,
            "moves": 1,
            "pos_red": [(3, 1)],
            "pos_purple": [],
            "pos_grey": [(0, 0), (1, 0), (4, 3)],
            "pos_white": [(1, 0), (2, 0), (4, 0), (4, 2)],
        },
        {  # 13
            "cols": 6,
            "rows": 3,
            "moves": 2,
            "pos_red": [(2, 3)],
            "pos_purple": [],
            "pos_grey": [(0, 0), (0, 4), (0, 5)],
            "pos_white": [(0, 3), (0, 4), (1, 1), (2, 1)],
        },
        {  # 14
            "cols": 4,
            "rows": 4,
            "moves": 2,
            "pos_red": [(3, 3)],
            "pos_purple": [],
            "pos_grey": [(0, 3), (2, 0), (3, 0)],
            "pos_white": [(1, 0), (1, 2), (2, 1), (2, 2)],
        },
        {  # 15
            "cols": 5,
            "rows": 3,
            "moves": 2,
            "pos_red": [(2, 2)],
            "pos_purple": [(1, 2)],
            "pos_grey": [(0, 1), (0, 3)],
            "pos_white": [(0, 0), (0, 2), (1, 4), (2, 4)],
        },
        {  # 16
            "cols": 5,
            "rows": 5,
            "moves": 3,
            "pos_red": [(2, 0)],
            "pos_purple": [(2, 4)],
            "pos_grey": [(1, 2), (3, 2)],
            "pos_white": [(0, 3), (0, 4), (4, 0), (4, 3)],
        },
        {  # 17
            "cols": 4,
            "rows": 4,
            "moves": 2,
            "pos_red": [(0, 0)],
            "pos_purple": [(3, 3)],
            "pos_grey": [(0, 2), (2, 0)],
            "pos_white": [(1, 1), (1, 3), (2, 2), (3, 1)],
        },
        {  # 18
            "cols": 6,
            "rows": 5,
            "moves": 2,
            "pos_red": [(4, 2)],
            "pos_purple": [(4, 3)],
            "pos_grey": [(0, 3), (2, 0), (2, 5)],
            "pos_white": [(1, 3), (2, 1), (2, 2), (2, 3), (2, 5)],
        },
        {  # 19
            "cols": 5,
            "rows": 5,
            "moves": 4,
            "pos_red": [(2, 2)],
            "pos_purple": [(0, 2)],
            "pos_grey": [(0, 1), (0, 3), (4, 1), (4, 3)],
            "pos_white": [(1, 0), (1, 4), (2, 1), (3, 0), (3, 2), (3, 4)],
        },
        {  # 20
            "cols": 4,
            "rows": 5,
            "moves": 2,
            "pos_red": [(4, 3)],
            "pos_purple": [(4, 2)],
            "pos_grey": [(0, 1), (0, 2), (4, 0)],
            "pos_white": [(0, 1), (0, 3), (1, 0), (2, 0), (3, 0)],
        },
        {  # 21
            "cols": 4,
            "rows": 3,
            "moves": 2,
            "pos_red": [(2, 3)],
            "pos_purple": [(2, 0)],
            "pos_grey": [(0, 1), (1, 1), (1, 2)],
            "pos_white": [(0, 2), (1, 0), (1, 1), (2, 0), (2, 1)],
        },
        {  # 22
            "cols": 5,
            "rows": 4,
            "moves": 3,
            "pos_red": [(3, 2)],
            "pos_purple": [(0, 0)],
            "pos_grey": [(0, 3), (0, 4), (3, 0)],
            "pos_white": [(0, 1), (0, 3), (1, 0), (1, 4), (2, 1)],
        },
        {  # 23
            "cols": 5,
            "rows": 4,
            "moves": 3,
            "pos_red": [(3, 2)],
            "pos_purple": [(3, 4)],
            "pos_grey": [(0, 3), (1, 4), (2, 0)],
            "pos_white": [(0, 2), (2, 1), (2, 2), (2, 3), (3, 2)],
        },
        {  # 24
            "cols": 5,
            "rows": 5,
            "moves": 3,
            "pos_red": [(3, 0)],
            "pos_purple": [(1, 4)],
            "pos_grey": [(0, 1), (1, 3), (3, 4)],
            "pos_white": [(0, 3), (2, 1), (2, 3), (4, 1), (4, 2)],
        },
        {  # 25
            "cols": 4,
            "rows": 5,
            "moves": 3,
            "pos_red": [(0, 3)],
            "pos_purple": [(4, 0)],
            "pos_grey": [(0, 0), (1, 2), (3, 2), (4, 3)],
            "pos_white": [(0, 0), (0, 3), (2, 0), (4, 0), (4, 1), (4, 2)],
        },
    ]

    def run(self):
        while True:
            var = input("Enter S: START THE GAME, E: Exit\n")
            if var.upper() == "S":
                try:
                    level = int(input("Enter Level number: 1 -> 25\n")) - 1
                    if level >= 0 and level < len(self.levels):
                        Game(self.levels[level])
                    else:
                        print("Invalid level")
                        continue
                except ValueError:
                    print("Invalid level")

            elif var.upper() == "E":
                break
            else:
                continue


if __name__ == "__main__":
    main().run()
