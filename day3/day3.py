from collections import Counter


def part1(lines):
    rev = {"0":"1", "1": "0"}
    gamma =""
    epsilon =""
    n = len((lines[0].strip()))
    for i in range(n):
        data = (line[i] for line in lines)
        count = Counter(data)
        x = max(count, key = count.get)
        gamma += x
        epsilon +=rev[x]
    print(int(gamma,2)* int(epsilon,2))
        
    

    

def part2(lines):
    def generate(lines, C_O2):
        for i in range(n):
            data = (line[i] for line in lines)
            count = Counter(data)  
            if C_O2 == "O2":          
                x = max(count, key = count.get)
                if count["0"] == count["1"]:
                    x = "1"
            else :
                x= min(count, key = count.get)
                if count["0"] == count["1"]:
                    x = "0"
            lines = [line for line in lines if line[i]==x ]
        return lines[0]
    n = len((lines[0].strip()))
    print(int(generate(lines, "O2"),2)*int(generate(lines, "CO2"),2))

    
        
            

            




if __name__ == "__main__":
    lines =[]
    with open("inputs.txt") as file:
        lines = file.readlines()
    part1(lines)
    part2(lines)
        
