def calPoints(operations : list[str]) -> int : 
    record = [] 
    sum = 0 
    record.append(int(operations[0]))
    for i in operations[1:]: 
             
        if i == "+": 
            record.append(record[-1] + record[-2]) 
        elif i == "D": 
            record.append(record[-1]*2) 
        elif i =="C": 
            record.pop() 
        else : 
            record.append(int(i))
        print(record)
        
    for i in record : 
        sum = sum + i 
    return sum  



if __name__ == '__main__': 
    assert calPoints(['5' , '2' , 'C' , 'D' , '+']) == 30 , 'the record should equal 30 not {}'.format(calPoints(['5' , '2' , 'C' , 'D' , '+']))
    assert calPoints(["5" , "-2" , "4" , "C" , "D" , "9" , "+" , "+"]) == 27 ,  'this should equal 27 not {}'.format(calPoints(["5" , "-2" , "C" , "D" , "9" , "+" , "+"]))
    assert calPoints(["1" , "C"]) == 0 , 'this should be zero ' 
    print('all tests passed successfully')
