def main():
    position = {"forward":0, "down":0, "up":0}
    with open("input.txt") as file:
        for line in file:
            instruction = line.strip().split()
            position[instruction[0]] += int(instruction[1])
    
    horizontal = position["forward"]
    depth =  position["down"] - position["up"]
    print(horizontal * depth)

            




if __name__ == "__main__":
    main()