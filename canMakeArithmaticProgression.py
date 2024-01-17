def canMakeArithmaticProgression(arr : list[int]) -> bool: 
    arr.sort()
    arithmatic_list = []
    arithmatic_list.append(arr[0]) 
    dif = arr[1] - arr[0]
    for i in range(1 , len(arr)  ): 
        arithmatic_list.append(arr[i-1] + dif)
    print('the original array : {} \n the arithmatic version of it : {}'.format(arr , arithmatic_list))
    if arithmatic_list == arr : 
        return True 
    else : 
        return False 

if __name__ =='__main__': 
    assert canMakeArithmaticProgression([1,3,5,7,9]) == True , 'this should be true '
    assert canMakeArithmaticProgression([1,8,15]) == True , 'this should be True ' 
    assert canMakeArithmaticProgression([4,3,2 , 9]) == False , 'this is should be return False'
    assert canMakeArithmaticProgression([1,2,2,2]) == False , 'this should be false'
    print('all tests passed ')