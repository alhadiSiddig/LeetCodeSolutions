def isMonotonic(nums : list[int]) -> bool : 

    des_comparing_list = nums.copy()
    des_comparing_list.sort(reverse = True)
    #sorted descendtly copy of nums 
    asc_comparing_list = nums.copy()
    asc_comparing_list.sort(reverse = False)
    if des_comparing_list == nums or asc_comparing_list == nums : 
        return True 
    else : 
        return False 
    
if __name__ =='__main__': 
    assert isMonotonic([1,2,2]) == True  , 'this should return True'
    assert isMonotonic([3,4,5,6]) == True , 'this should return True' 
    assert isMonotonic([3,5,2]) == False , 'this should return fasle value '
    print('all tests passed')