def toLowerCase(s: str) -> str: 
    return s.lower() 






if __name__ == '__main__': 
    assert toLowerCase('Hello') == 'hello' , 'this should be hell' 
    assert toLowerCase('here') =='here' , 'this should be here too' 
    assert toLowerCase('LOVELY') =='lovely' , 'this should be lovely' 
    print('all test passed successfully')

