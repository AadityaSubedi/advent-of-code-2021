from collections import Counter

def part1(data):
    return sum(sum(1 for op in item if len(op) in unique)  for item in data)

# def part2(data):
#     sum=0
#     for item in data:
#         display=""
#         for output in item:
#             x = str([i for i,value in seven_seg.items() if "".join(sorted(value))== "".join(sorted(output))])
#             print(x)
#             # print(output)
#             # display+=x
#         # sum+= int(display)
#         # print(display)
#     return sum

if __name__ == "__main__":
    with open("testinput.txt") as file:
        data = [item.strip().split("|")[1].split() for item in file.readlines()]

    unique = [2,4,3,7]
    seven_seg = {
        0:"cagedb",
        1: "ab",
        2:"gcdfa",
        3:"fbcad",
        4:"eafb",
        3:"cdfbe",
        6:"cdfgeb",
        7:"dab",
        8:"acedgfb",
    }
    x = part2(data)
    print(x)
