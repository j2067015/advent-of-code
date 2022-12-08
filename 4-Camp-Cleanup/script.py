with open("4-Camp-Cleanup/input.txt", "r") as file:
    fd = file.read().strip().split()


def part_one():
    count = 0
    for line in fd:
        first_elf, second_elf = line.split(",")
        first_elf[:] = int(*first_elf.split("-"))
        second_elf = second_elf.split("-")
        print(first_elf)
        
    # print(count)

        


        

part_one()