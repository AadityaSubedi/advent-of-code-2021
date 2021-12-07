from collections import Counter


def quad_fuel(steps):
    return steps*(steps+1)/2 if steps else 0


# this fn is redundant, used here only to make uniform with part2
def linear_fuel(steps):
    return steps


def part1(positions):
    min_fuel = float("inf")
    for key in range(max(positions)):
        min_fuel = min(sum(linear_fuel(abs(k-key))*count for k,
                       count in positions.items()), min_fuel)
    return min_fuel


def part2(positions):
    min_fuel = float("inf")
    for key in range(max(positions)):
        min_fuel = min(sum(quad_fuel(abs(k-key))*count for k,
                       count in positions.items()), min_fuel)
    return min_fuel


if __name__ == "__main__":
    with open("input.txt") as file:
        positions = Counter(int(item)
                            for item in file.readline().strip().split(","))
    x = part1(positions)
    print(x)
    y = part2(positions)
    print(y)
