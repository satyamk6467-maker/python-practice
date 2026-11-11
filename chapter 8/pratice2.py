# write a program to read a text from a given file certificate .txt
#and find 
#wether it contains the word live 
file= open("certificate.txt","r")
dataofFile= file.read()
dataofFile= dataofFile.lower()

if "live" in dataofFile:
    print("yes live word is present in the file ")
else:
    print("no ")