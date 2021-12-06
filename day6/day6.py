from collections import Counter

def score(initial, day):
    for i in range(day):
        x =0
        Y = {}
        for j , count in initial.items():
            if j ==0:
                x  = count
            else:
                Y[j-1] = count
        Y[8] =x
        Y[6]+=x
        initial = Y    

    return sum(initial.values())


        
        



def part1(initial):
    return score(initial, 80)



def part2(initial):
    return score(initial, 256)



if __name__ == "__main__":
    with open("input.txt") as file:
        initial = Counter(int(item) for item in file.readline().strip().split(","))
    # set uninitialize key with 0
    for i in range(9):
        initial[i] = initial.get(i, 0)
    x = part1(initial)
    print(x)
    y = part2(initial)
    print(y)









