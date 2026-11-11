# open a file called report.txt in write mode.
file = open("report.txt","a")
file.write("hii satyam , belive in your self, satyam just belive your self  ")
file.close()

with open("report.txt","r") as f:
    data= f.read()
    print('file data')
