import sys
with open("test.txt",'r') as f:
    for line in f:
        data = line.strip().split(',')
        playing  = True
        initial = 0
        print(data)
        while(playing):
            match int(data[initial]):
                case 1:
                    data[int(data[initial+3])]=int(data[int(data[initial+2])])+int(data[int(data[initial+1])])
                    print(f"the operation was one and the data set became {data} ")
                case 2:
                    data[int(data[initial+3])]=int(data[int(data[initial+2])])*int(data[int(data[initial+1])])
                    print(f"the operatin was 2 and the data set became {data} ")
                case 99:
                    print(data[0])
                    print("program compelted")
                    sys.exit()
                case _:
                    print("some error occured")
                    sys.exit()
            initial+=4
            



        
