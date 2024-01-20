def lemonadeChange(bills : list[int] )  -> bool : 
        five  = ten = 0 
        for i in bills : 
            if i ==5 : 
               five  = five + 1 
            elif i ==5  : 
                five , ten = five -1 , ten + 1 
            elif i == 10 : 
                 five ,ten  = five -1 , ten - 1 
            elif ten>  0 :
                five , ten  = five -1 , ten -1 
            else : five -=3 
            if five < 0 : return False 
        return True 
                


if __name__ == '__main__': 
    assert lemonadeChange([5,10]) == True , '1st test : this should be True ' 
    assert lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5])  == True , 'this should be false , 2nd test '
    assert lemonadeChange([5,5,5,10,20]) == True , '3rd test , should be True ' 
    assert lemonadeChange([5,5,10 ,10 , 20]) == False , '4th test : some thing went wrong review yoru calacultions '
    assert lemonadeChange([5,5,10 ,10 , 10 ,  20]) == False , 'fth test :some thing went wrong review yoru calacultions '

    print('all tests passed ')