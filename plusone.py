def plusOne(digits: list[int] )-> list[int]: 
    place_holder = []
    digits_int = int(''.join(str(i) for i in digits))
    digits_int = digits_int + 1 
    digits_str = str(digits_int)  
    for i in digits_str: 
        place_holder.append(int(i))
    return place_holder
        


if __name__ =='__main__': 
    print(plusOne([9]))
    assert plusOne([1,2,3,4,5]) == [1,2,3,4,6] , 'those should be equale' 
    assert plusOne([3,3,4,2]) == [3,3,4,3] , 'those two should be equale' 
    assert plusOne([9]) == [1,0] , 'should be two element  , the base ten should not appear any where '
    print('all tests passed') 
