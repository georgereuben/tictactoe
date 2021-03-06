class grid:
    def __init__(self, arr):
        self.arr = arr
        self.x = [" xx      xx ", "   xx  xx   ", "     xx     ", "   xx  xx   ",
                  " xx      xx "]  # arrays storing each line of the input
        self.o = ["    oooo    ", "  oo    oo  ",
                  " oo      oo ", "  oo    oo  ", "    oooo    "]
        self.none = ["            ", "            ",
                     "            ", "            ", "            "]
        # 0 is unmarked square, 1 is player one's input, 2 is player two's input
        self.dict = {0: self.none, 1: self.x, 2: self.o}
        self.hline = "---------------|--------------|---------------"

    def print_grid(self):  # prints the grid using the dict function
        for i in range(3):
            for j in range(5):
                print('|', self.dict[self.arr[i][0]][j], '|', self.dict[self.arr[i][1]][j],
                      '|', self.dict[self.arr[i][2]][j], '|')  # Prints each line in the output
            if i < 2:  # if i is less than two, prints the horizontal line between the elements
                print(self.hline)

    def grid_checker(self):  # function to check if the game has ended after a turn
        for i in range(3):
            if (self.arr[i][0] == self.arr[i][1] and self.arr[i][1] == self.arr[i][2]):  # checking rows
                return self.arr[i][0]
            # checking columns
            elif (self.arr[0][i] == self.arr[1][i] and self.arr[1][i] == self.arr[2][i]):
                return self.arr[0][i]
        # checking left to right diagonal
        if (self.arr[0][0] == self.arr[1][1] and self.arr[1][1] == self.arr[2][2]):
            return self.arr[1][1]
        # checking right to left diagonal
        elif (self.arr[0][2] == self.arr[1][1] and self.arr[1][1] == self.arr[2][0]):
            return self.arr[1][1]
        else:
            return 4  # continues to the next turn
