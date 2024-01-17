def arraySign(array : list[int])-> list[int]: 
    def checker(x,y):
        if x * y > 0 : 
            return 1 
    if map(checker , array) ==  0 : return 0 
    elif map (checker , array)> 0 : return 1 
    else : return -1 

def arraySign(nums: list[int]) -> list[int]: 
    
    if 0 in nums : 
        return 0 
    if len([i for i in nums if i < 0 ])%2 == 0 : 
        return 1 
    else : 
        return -1
    

if __name__ =='__main__': 
    assert arraySign([-1,-2,-3,-4 , 3,2,1]) == 1 , 'this should be 1 cause there is four negative numbers ' 
    print('test passed')