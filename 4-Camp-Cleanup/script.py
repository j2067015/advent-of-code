with open("4-Camp-Cleanup/input.txt", "r") as file:
    fd = file.read().strip().split()


def part_one():
    count = 0
    for line in fd:
        first_elf, second_elf = line.split(",")
        first_elf = first_elf.split("-")
        first_elf[:] = int(first_elf[0]), int(first_elf[1])
        second_elf = second_elf.split("-")
        second_elf[:] = int(second_elf[0]), int(second_elf[1])
        
        if (first_elf[1] >= second_elf[1]) and (first_elf[0] <= second_elf[0]):
            count += 1
        elif (first_elf[1] <= second_elf[1]) and (first_elf[0] >= second_elf[0]):
            count += 1
        
    print(count)

def part_two():
    count = 0
    for line in fd:
        first_elf, second_elf = line.split(",")
        first_elf = first_elf.split("-")
        first_elf[:] = int(first_elf[0]), int(first_elf[1])
        second_elf = second_elf.split("-")
        second_elf[:] = int(second_elf[0]), int(second_elf[1])

        if (first_elf[1] > second_elf[1]):
            larger = first_elf
            smaller = second_elf
        elif (second_elf[1] > first_elf[1]):
            larger = second_elf
            smaller = first_elf
        else:
            count += 1
            continue
        

        if larger[0] <= smaller[1]:
            count += 1
        
    print(count)


        

part_two()