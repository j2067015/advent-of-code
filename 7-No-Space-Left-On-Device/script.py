with open("7-No-Space-Left-On-Device/input.txt", "r") as file:
    fd = file.read().strip().split("\n")

def part_one():
    for line in fd:
        print(line)
        if line[0] == '$':
            line = line.split(" ")
            match line[0]:
                case "ls":

                case "cd":
                    
        else:
            line = line.split(" ")

part_one()