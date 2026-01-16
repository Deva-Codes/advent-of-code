
def findoutput(x,y,originaldata):
    playing = True
    data = originaldata.copy()
    data[1] = x
    data[2] = y
    initial =0
    

    while playing:
        operator = int(data[initial])
        operand1 = int(data[int(data[initial+1])])
        operand2 = int(data[int(data[initial+2])])
        targetposition = int(data[initial+3])
        match operator:
                case 1:
                    data[targetposition] = operand1 + operand2
                case 2:
                    data[targetposition] = operand1 *operand2
                case 99:
                    return data[0]
                    playing = False
        initial+=4

with open ("test.txt",'r') as f:
    for line in f:
        data= line.strip().split(',')
    for x in range(100):
        for y in range(100):
            if(findoutput(x,y,data)==19690720):
                print(100 *x+y)

