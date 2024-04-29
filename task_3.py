from collections import OrderedDict


def print_towers(towers: dict):
    for tower in sorted(list(towers.keys())):
        print(f"{tower}: {towers[tower]}", end=" ")
    print()


def move_tower(disk, towers: dict):
    ordered_list = list(towers.items())
    source = {ordered_list[0][0]: ordered_list[0][1]}
    dest = {ordered_list[2][0]: ordered_list[2][1]}
    temp = {ordered_list[1][0]: ordered_list[1][1]}

    if disk == 1:
        ordered_list[2][1].append(ordered_list[0][1].pop())
        print(f"Move disk {disk} from {ordered_list[0][0]} to {ordered_list[2][0]}")
        print_towers(towers)

    else:
        towers = {**source, **dest, **temp}
        towers = OrderedDict(towers)
        move_tower(disk - 1, towers)
        ordered_list[2][1].append(ordered_list[0][1].pop())
        print(f"Move disk {disk} from {ordered_list[0][0]} to {ordered_list[2][0]}")
        towers = {**temp, **source, **dest}
        print_towers(towers)
        towers = OrderedDict(towers)
        move_tower(disk - 1, towers)


def hanoi(disks_number: int):
    towers = OrderedDict({'A': list(range(disks_number, 0, -1)), 'B': [], 'C': []})
    move_tower(disks_number, towers)


if __name__ == "__main__":
    disks = int(input("Enter the number of disks: "))
    hanoi(disks)
