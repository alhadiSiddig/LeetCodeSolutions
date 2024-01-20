def average(salary : list[int]) -> float : 
   salary = sorted(salary , reverse = False)
   value = sum(salary[1:-1])//(len(salary[1:-1])) 
   print(value) 
   return value 
    
if __name__ == '__main__': 
    assert average([4000 , 3000 , 1000 , 2000 ]) == 2500 , 'the answer is not 2.500, something went wrong ' 
    assert average([1000 , 2000 , 3000]) == 2000 , 'something went wrong , correct answer is 1000' 
    print('all tests passed successfully')