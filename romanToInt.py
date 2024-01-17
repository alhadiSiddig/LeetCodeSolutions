def romanToInt(s : str ) -> int : 
    values_list = []
    sum : int = 0  
    roman_numerals = {'I': 1 , 'V' : 5 , 'X' : 10 , 
                      'L' : 50 , 'C' : 100 , 'D': 500 ,
                      'M': 1000}
    values_list.append(roman_numerals[s[0]])
    for i in s[1:] : 
        values_list.append(roman_numerals[i]) 
        if values_list[-1] > values_list[-2]: 
           large_value = values_list.pop()
           small_vlaue = values_list.pop() 
           values_list.append(large_value - small_vlaue)
    for i in values_list : 
        sum  = sum  + i
    return sum 
           

if __name__ == '__main__': 

    assert romanToInt("III") == 3 , '{} does not equal three'.format(romanToInt('III'))
    assert romanToInt("LVIII") == 58 , 'this should be fifty eight ' 
    assert romanToInt('MCMXCIV') == 1994 , '{} does not equal 1944'.format(romanToInt('MCMXCIV')
    )
