

def main():
    count = 0
    prev = float("-inf")
    isFirst = True
    with open("input.txt") as file:
        for line in file:
            if isFirst:
                isFirst  = False
                prev = int(line)
                continue
            if not isFirst  and int(line) > prev:
                count +=1 
            prev = int(line)

    print(count)
            




if __name__ == "__main__":
    main()