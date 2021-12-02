def main():
    position = {"forward":0,  "aim":0, "depth":0}
    with open("testinput.txt") as file:
        for line in file:
            instruction = line.strip().split()
            instruct = instruction[0]
            value = int(instruction[1])
            if instruct == "up":
                position["aim"]-=value
            elif instruct == "down":
                position["aim"]+=value
            elif instruct == "forward":
                position["forward"] += value
                position["depth"] += position["aim"]* value
    
    horizontal = position["forward"]
    depth =  position["depth"]
    print(horizontal * depth)

            




if __name__ == "__main__":
    main()