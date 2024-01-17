def is_anagram(word1 , word2):
         if len(word1) != len(word2): return False
         for i in word1 :
             if i in word2 :
                  word2 = word2.replace(i , '' , 1)
             else : return False
             print(word1 , word2)
         if len(word2) == 0 : return True
         else : return False
