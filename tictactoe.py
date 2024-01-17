def tictactoe(moves : list[list[int]]) -> str : 
    #split the moves list into two lists , using index : 
    the_original_place = {1: [0 , 0 ],2 : [0,1] , 3 : [0,2] , 
                          4: [1 , 0 ],5 : [1,1] , 6 : [1,2] , 
                          7 : [2, 0 ] , 8 : [2,1] , 9 : [2,2]}
    
    player_one = [] 
    player_two = []
    
    for i in moves[2:] : 
        if moves.index(i) % 2 == 0 : 
            player_one.append(i)
        else : 
            player_two.append(i) 

    print(player_one , player_two)

if __name__ == '__main__': 
    assert tictactoe([[0,0] , [2,0] , [1,1] , [2,1]  , [2,2]])

