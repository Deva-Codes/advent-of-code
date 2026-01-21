import sys

with open("test.txt",'r') as f:
    for line in f:
        data = line.strip().split(',')
        initial = 0 #the starting index form where the loop should start
        while(True):
            match int(data[initial]):
                case 1:
                    data[int(data[initial+3])]=int(data[int(data[initial+2])])+int(data[int(data[initial+1])])
                case 2:
                    data[int(data[initial+3])]=int(data[int(data[initial+2])])*int(data[int(data[initial+1])])   
                case 99:
                    print(data[0])
                    print("program compelted")
                    sys.exit()
                case _:
                    print("some error occured")
                    sys.exit()
            initial+=4
            



        
