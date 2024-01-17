def judgeCircle(moves : str) -> bool: 
    vertical : bool = False 
    horizntal : bool = False 
    if moves.count("U") == moves.count('D') : 
       vertical = True 
    if moves.count('L') == moves.count('R'): 
        horizntal = True 
    if vertical & horizntal : 
        return True 
    else : 
        return False 
    
                




if __name__ =='__main__': 
    assert judgeCircle ('LL') == False , 'this is not a circle ' 
    assert judgeCircle('UD') == True  ,'the robot return to its origianl point on plane'
    print (" all tests passed successfully")