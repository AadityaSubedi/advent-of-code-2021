from collections import Counter




def checkRows(board):
    # for row in board:
    return any(all((cell == -1 for cell in row)) for row in board)



def checkCols(board):
    result = []
    for col in range(len(board[0])):
        result.append(all((board[row][col] == -1 for row in range(len(board)))))
    return any(result) 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return checkRows(board) or checkCols(board)

def score(board):
    return sum([sum([int(cell)  for cell in row if int(cell) != -1]) for row in board])


def part1(boards, drawer):
    for el in drawer:
        # mark the element in each board 
        for k, board in enumerate(boards):
            for i,row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == el:
                        boards[k][i][j]= -1
        # check if the winner:
        for board in boards:
            if winner(board):
                return score(board) * int(el)

    

        
    

    

def part2(boards, drawer):
    for el in drawer:
        if el in drawer[:5]:
            continue
        # mark the element in each board 
        for k, board in enumerate(boards):
            for i,row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == el:
                        boards[k][i][j]= -1
        # check if the winner:
        for board in boards:
            if winner(board):
                # return score(board) * int(el)
                if len(boards)>1  :
                    boards.remove(board)
                else:
                    return score(board) * int(el)
    
        
            

            




if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
    drawer = lines[0].strip().split(",")
    boards=[]
    for i in range(2,len(lines)-4,6):
            boards.append(lines[i:i+5])
    boards = [[row.strip().split() for row in board] for board in boards]
    print(part1(boards, drawer))
    
    




    
        
