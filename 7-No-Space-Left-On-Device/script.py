with open("7-No-Space-Left-On-Device/input.txt", "r") as file:
    fd = file

directories = []

def part_one():
    while 1:
        line = fd.readline().strip("\n").replace("$ ", "").split(" ")
        match line[0]:
            case "ls":
                while 1:
                    dir_search = fd.readline().strip("\n")
                    if dir_search[0] == "$":
                        break
                    dir_search = dir_search.split(" ")
            case "cd":

            case "dir":


            case _:


            



def add_to_dir():


part_one()