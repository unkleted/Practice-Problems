# Problem 15
#
# Starting in the top left corner of a 2x2 grid, and only being able to move to 
# the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?


from timeit import time_func

def make_list(num):
    foo = []
    for i in range(num):
        foo.append('')
    return foo


@time_func
def main():
    grid = []
    grid_rows = 21

    for i in range(grid_rows):
        grid.append(make_list(grid_rows))

    for i in range(grid_rows):
        for j in range(grid_rows):
            if i == 0 or j== 0:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

    print(grid[20][20])


if __name__ == "__main__":
    main()