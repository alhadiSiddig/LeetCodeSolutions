#this solution isn't mine, i copies it from else where, though i liked it . 


def tictactoe(moves : list[list[int]]) -> str : 
    winner = None 

    matrix = [[0 for _ in range(3)]  for _ in range(3)] 
    

    for i , (x,y) in enumerate(moves): 
        matrix[x][y] = 5 if i & 1 else 1 

    def checkWin(s): 
        nonlocal winner 
        if s == 3 : 
            winner = 'A' 
        if s == 15 : 
            winner = 'B' 
    def checkRows(): 
        for row in matrix : checkWin(sum(row)) 
    def checkCols(): 
        for col in zip(*matrix): 
            checkWin(sum(col)) 
    def checkDiagonal(): 
        checkWin(matrix[0][0] + matrix[1][1] + matrix[2][2]) 
        
    def checkDiagonal2(): 
        checkWin(matrix[0][2] + matrix[1][1] + matrix[2][0]) 

    
    checkRows() 
    checkCols() 
    checkDiagonal() 
    checkDiagonal2() 
    return winner or ('Draw' if len(moves) == 9 else 'pending ')
    
if __name__ =='__main__': 
    assert tictactoe([[0,0],[2,0] , [1,1], [2,1] , [2,2]]) == 'A' , 'player B is not the winner, A is  ' 
    print('all tests passed ') 