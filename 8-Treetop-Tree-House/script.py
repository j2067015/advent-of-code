with open("8-Treetop-Tree-House/input.txt", "r") as file:
    grid = file.read().strip().split()

def part_one():
    count = 0
    for r in range(1, len(grid)-2):
        for c in range(1, len(grid[r])-2):
            #        up,            down,         left,         right
            nearby = [grid[r-1][c], grid[r+1][c], grid[r][c-1], grid[r][c+1]]
            for value in nearby:
                if value > grid[r][c]:
                    break
            else:
                count += 1
            
    print(count)
            




part_one()