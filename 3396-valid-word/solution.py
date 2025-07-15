class Solution:
    def isValid(self, word: str) -> bool:
        vowel = ['a','e','i','o','u']
        vpass = False
        consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']     
        cpass = False
        npass = False
        apass = False   
        if len(word) < 3:
            print(1)
            return False
        for i in word:
            j = i.lower()
            if 48 <= ord(i) <= 57:
                pass
            elif 65 <= ord(i) <= 90:
                pass
            elif 97 <= ord(i) <= 122:
                pass
            else:
                print(i)
                print(2)
                return False
            if j in vowel and not vpass:
                vpass = True
            if j in consonant and not cpass:
                cpass = True
        if not vpass or not cpass:
            print(i)
            print(3)
            return False
        else:
            print(0)
            return True
            
            
