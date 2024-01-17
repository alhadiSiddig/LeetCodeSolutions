def lengthOfLastWord(s: str) -> int : 
    return len(s.rstrip().split(' ')[-1])
def lengthOfLastWord_2(s : str) -> int : 
    s = s.rstrip() 
    last_word = '' 
    for i in s[::-1] : 
        if i != ' ': 
            last_word = last_word + i 
        else : 
            break

    return len(last_word[::-1])

            

    


if __name__ == '__main__': 
    assert lengthOfLastWord('Hello World') == 5 , 'the last word length should be five '
    assert lengthOfLastWord('     fly me to   the moon   ') == 4 , 'the length of the last word is four' 
    assert lengthOfLastWord('luffy is still joyboy') == 6 , '6 and not else'
    print("all tests for first version passed")
    assert lengthOfLastWord_2('Hello World') == 5 , 'the last word length should be five '
    assert lengthOfLastWord_2('     fly me to   the moon   ') == 4 , 'the length of the last word is four' 
    assert lengthOfLastWord_2('luffy is still joyboy') == 6 , '6 and not else'
    print("all tests for second version passed")