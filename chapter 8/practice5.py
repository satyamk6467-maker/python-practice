# Read only the first line of bio.txt
with open("bio.txt","r") as f:
    line1= f.readline()
    print("line1",line1)
