"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:

Input: s = "aba"
Output: false

Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""
import unittest 

def is_subStringPattern(s : str ) -> bool : 
    subString : str = s[:1]
    index_counter = 0 
    
    while index_counter <= len(s)/2: 
        if len(s) == 1 : 
            return True 
        if s.count(subString) == len(s)/len(subString):
            return True
        else : 
           
           index_counter = index_counter + 1 
           subString = s[:index_counter]
    return False 
        
def is_subStringPattern_0_1(s:str) -> bool : 
    n  = len(s ) 
    for i in range(1 , n//2 +1) : 
        if n % i == 0 : 
            substring = s[:i]
            if substring * (n//i) == s : 
                return True
def is_subStringPatter_0_2(s:str) -> bool: 
    return s in (s+s)[1:-1]


class TestPattern(unittest.TestCase): 
    def is_subStringPattern(self):
        self.assertEqual(is_subStringPattern('ababab') , True )  

 

if __name__ == '__main__':
    assert is_subStringPattern('abababab') == True , 'this should be True '
    assert is_subStringPattern('abdbabab') == False , 'this should be False '
    assert is_subStringPattern('abab')==True , 'this should be True ' 
    assert is_subStringPattern('adada') ==False , 'this should be false '
    assert is_subStringPattern('a')==True  , 'this should be True'
    print('all test passed successfully') 

