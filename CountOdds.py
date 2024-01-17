def countOdds(low : int , high : int) -> int : 
    if low%2 == 0 and high%2 == 0 : 
        return (high - low )/2 
    if low%2 == 1 and high%2 ==1 or low%2 == 0 and high%2 == 1 or low%2 == 1 and high%2 == 0 : 
        return (high-low)/2 + 1 
    
if __name__ == '__main__': 
    assert countOdds(3,7) == 3 , 'three number including both the low and high ' 
    assert countOdds(8 ,10) == 1  , 'this should be 1 ' 

    print("all tests passed ")