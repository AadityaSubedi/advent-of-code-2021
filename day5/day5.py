import math, copy
def draw_line(line, graph):
    x1 = int(line[0][0])
    y1 = int(line[0][1])
    x2 = int (line[1][0])
    y2 = int (line[1][1])

    # SGN function implement
    sign = lambda x: bool(x > 0) - bool(x < 0)
    lx = sign(x2-x1)
    ly = sign(y2-y1)
    
    while (x1,y1) != (x2+lx,y2+ly):
        graph[y1][x1] +=1
        x1+=lx
        y1+=ly
        





def generate_score(lines):
    # identify the  max coordinate
    x =0
    y=0
    for line in lines:
       for point in line:
           x = max(x,int(point[0]))
           y = max(y,int(point[1]))

    #  construct a matrix to represent graph
    graph = [[0]*(x+1) for _ in range(y+2) ]
    

    for line in lines:
        draw_line(line, graph)

    score = sum(sum([k >1 for k in row]) for row in graph)
    return score
            


def part1(lines):
    # only those lines with x1 = x2 or y1 = y2
    # horizontal or vertical lines only
    lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]
    return generate_score(lines)

def part2(lines):
    return generate_score(lines)
    

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [[point.split(",")for point in line.strip().split(" -> ")] for line in file.readlines()]
    print("part1", part1(lines))
    print("part2", part2(lines))
    




    
        
