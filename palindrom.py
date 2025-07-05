def ispalindrom(arr):
    palindroms = []
    for word in arr:
        if word == word[::-1]:
            palindroms.append(word)
    
    return palindroms          
             
ispalindroms = ["level", "forest", "lair"]
print("This words are palindroms ==> ", ispalindrom(ispalindroms))

