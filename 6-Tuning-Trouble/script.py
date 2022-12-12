with open("6-Tuning-Trouble/input.txt", "r") as file:
    fd = file.read().strip()

def part_one():
    buffer = []
    for i, char in enumerate(fd):
        buffer.append(char)
        if i >= 4:
            if (len(buffer) == len(set(buffer))):
                print(i)
                exit()
            buffer.pop(0)


def part_two():
    buffer = []
    for i, char in enumerate(fd):
        buffer.append(char)
        if i >= 14:
            if (len(buffer) == len(set(buffer))):
                print(i)
                exit()
            buffer.pop(0)

part_one()