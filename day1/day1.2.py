

def main():
    prevSum =0 
    inc=0
    isFirst = True
    with open("input.txt") as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        # print(i,line)
        presentSum = 0
        try:
            presentSum+= int(line) +int(lines[i+1]) + int(lines[i+2])
        except IndexError:
            break
        
        print(presentSum)
        if isFirst:
            isFirst = False
            prevSum = presentSum
            continue
        if presentSum > prevSum:
            inc +=1 
        prevSum = presentSum
        








            

    print(inc)
            




if __name__ == "__main__":
    main()