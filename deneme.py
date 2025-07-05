#liste = ["1", "2", "5a", "10a", "abc", "10", "50" ]
#
#for x in liste:#
    #try:
        #x == int(x)
        #print(f"{x} is a number.")
    #
    #except ValueError:
        #continue
    
#while True:
    #choice = input("input:")
    #if choice == "q":
        #break
#
    #try:
        #result = int(choice)
        #print(f"{result} its a number.")
#
    #except ValueError:
        #print("its not a number.")
        #continue

#turkish_chars = 'şçİıüöğ'
#def check_password(password):
    #for i in password:
        #if i in turkish_chars:
            #raise TypeError("parola türkçe karakter içeremez.")
        #else:
            #pass
    #print("correct password")
#password = input("password: ")
#try:
    #check_password(password)
#except TypeError as err:
    #print(err)

#def factoriel(x):
    #x = int(x)
    #if x < 0:
        #raise ValueError('negatif değer')
    #result = 1
#
    #for i in range(1, x + 1):
        #result *= i
    #return result

#for x in [5, 10, -3, '10a']:
    #try:
        #y = factoriel(x)
    #except ValueError as err:
        #print(err)
        #continue
    #print(y)