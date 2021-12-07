from collections import Counter


        
def quad_fuel(steps):

    return steps*(steps+1)/2  if steps else 0     


# this fn is redundant, used here only to make uniform with part2
def linear_fuel(steps):
    return steps  



def part1(positions):
    fuels=[]
    for key in range(max(positions)):
        fuels.append(sum(linear_fuel(abs(k-key))*count for k,count in positions.items()))
    return min(fuels)
            


def part2(positions):
    fuels=[]
    for key in range(max(positions)):
        # print(list(quad_fuel(abs(k-key))*count for k,count in positions.items()))
        fuels.append(sum(quad_fuel(abs(k-key))*count for k,count in positions.items()))
    # print(fuels)
    return min(fuels)



if __name__ == "__main__":
    with open("input.txt") as file:
        positions = Counter(int(item) for item in file.readline().strip().split(","))
    x = part1(positions)
    print(x)
    y = part2(positions)
    print(y)









