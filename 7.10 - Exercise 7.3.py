import timeit

# looping method
candy_values = {}
def find_best_path(grid):
    for x in range(grid["size"][0]):
        for y in range(grid["size"][1]):
            current_candy = grid.get((x, y), 0)
            backtracking_above = 0
            if y > 0:
                backtracking_above = candy_values[(x, y-1)]
            backtracking_left = 0
            if x > 0:
                backtracking_left = candy_values[(x-1, y)]

            max_future_path = max(backtracking_above, backtracking_left)
            future_path = max_future_path + current_candy
            candy_values[(x,y)] = future_path
    return candy_values[((grid["size"][0] - 1), (grid["size"][1] - 1))]


if __name__ == "__main__":
    grid = {
        "size": (5,5),
        (1,0): 1,
        (1,1): 3,
        (1,2): 2,
        (1,3): 3,
        (2,2): 2,
        (2,3): 1,
        (4,3): 2
    }
    print(find_best_path(grid)) # should print 12

    grid = {
        "size": (5,6),
        (1,0): 1,
        (1,1): 3,
        (1,2): 2,
        (1,5): 3,
        (2,0): 2,
        (2,1): 3,
        (2,2): 2,
        (2,3): 1,
        (3,1): 3,
        (3,5): 2,
        (4,1): 3,
        (4,3): 2
    }
    print(find_best_path(grid)) # should print 15

    # efficiency test
    # ---------------
    # uncomment the code below to test with a 100 by 100 grid (uncomment a selection using Ctrl + r on windows or Cmd + r on a Mac)
    # this should complete in a fraction of a second, to pass the test you will need it to complete in less that 1 second

    grid = {
          "size": (99,99),
          (1,0): 1,
          (1,1): 3,
          (1,2): 2,
          (1,5): 3,
          (2,0): 2,
          (2,1): 3,
          (2,2): 2,
          (2,3): 1,
          (3,1): 3,
          (3,5): 2,
          (4,1): 3,
          (4,3): 2,
          (98,98): 3
    }
    start_time = timeit.default_timer()
    print(find_best_path(grid)) # should return and print 18
    end_time = timeit.default_timer()

    time_taken = end_time - start_time
    print(time_taken)


# recursive method with memoization
# This just calls the recursive method to start it
def find_best_path(grid):
    memo = {}
    return find_best_path_rec(grid["size"][0] - 1, grid["size"][1] - 1, grid, memo)


def find_best_path_rec(x, y, grid, memo):
    if x < 0 or y < 0:
        return 0

    if (x, y) in memo:
        return memo[(x, y)]

    current_sweet = grid.get((x, y), 0)
    max_future_path = max(find_best_path_rec(x - 1, y, grid, memo), find_best_path_rec(x, y - 1, grid, memo))
    future_path = current_sweet + max_future_path
    memo[(x, y)] = future_path
    return future_path


if __name__ == "__main__":
    grid = {
        "size": (5,5),
        (1,0): 1,
        (1,1): 3,
        (1,2): 2,
        (1,3): 3,
        (2,2): 2,
        (2,3): 1,
        (4,3): 2
    }
    print(find_best_path(grid)) # should return 12

    grid = {
        "size": (5,6),
        (1,0): 1,
        (1,1): 3,
        (1,2): 2,
        (1,5): 3,
        (2,0): 2,
        (2,1): 3,
        (2,2): 2,
        (2,3): 1,
        (3,1): 3,
        (3,5): 2,
        (4,1): 3,
        (4,3): 2
    }
    print(find_best_path(grid)) # should return 15

    # efficiency test
    # ---------------
    # uncomment the code below to test with a 100 by 100 grid (uncomment a selection using Ctrl + r on windows or Cmd + r on a Mac)
    # this should complete in a fraction of a second, to pass the test you will need it to complete in less that 1 second
    grid = {
    "size": (99,99),
        (1,0): 1,
        (1,1): 3,
        (1,2): 2,
        (1,5): 3,
        (2,0): 2,
        (2,1): 3,
        (2,2): 2,
        (2,3): 1,
        (3,1): 3,
        (3,5): 2,
        (4,1): 3,
        (4,3): 2,
        (98,98): 3
        }
    start_time = timeit.default_timer()
    print(find_best_path(grid)) # should return and print 18
    end_time = timeit.default_timer()
    time_taken = end_time - start_time
    print(time_taken)


# recursive method without memoization (never-ending)
# This just calls the recursive method to start it
def find_best_path(grid):
    return find_best_path_rec(grid["size"][0] - 1, grid["size"][1] - 1, grid)

# recursive method
def find_best_path_rec(x, y, grid):
    if x < 0 or y < 0:
        return 0
    current_sweet = grid.get((x, y), 0)
    max_future_path = max(find_best_path_rec(x-1, y, grid), find_best_path_rec(x, y-1, grid))
    future_path = current_sweet + max_future_path
    return future_path

if __name__ == "__main__":
    grid = {
        "size": (5,5),
        (1,0): 1,
        (1,1): 3,
        (1,2): 2,
        (1,3): 3,
        (2,2): 2,
        (2,3): 1,
        (4,3): 2
    }
    print(find_best_path(grid)) # should return 12

    grid = {
        "size": (5,6),
        (1,0): 1,
        (1,1): 3,
        (1,2): 2,
        (1,5): 3,
        (2,0): 2,
        (2,1): 3,
        (2,2): 2,
        (2,3): 1,
        (3,1): 3,
        (3,5): 2,
        (4,1): 3,
        (4,3): 2
    }
    print(find_best_path(grid)) # should return 15

    # efficiency test
    # ---------------
    # uncomment the code below to test with a 100 by 100 grid (uncomment a selection using Ctrl + r on windows or Cmd + r on a Mac)
    # this should complete in a fraction of a second, to pass the test you will need it to complete in less that 1 second
    grid = {
        "size": (99,99),
        (1,0): 1,
        (1,1): 3,
        (1,2): 2,
        (1,5): 3,
        (2,0): 2,
        (2,1): 3,
        (2,2): 2,
        (2,3): 1,
        (3,1): 3,
        (3,5): 2,
        (4,1): 3,
        (4,3): 2,
        (98,98): 3
    }
    start_time = timeit.default_timer()
    print(find_best_path(grid)) # should return and print 18
    end_time = timeit.default_timer()
    time_taken = end_time - start_time
    print(time_taken)