data = []
sum=0
with open("test.txt",'r') as f:
    for line in f:
        if(line.strip()!=""):
            sum+=int(line.strip())
        else:
            data.append(sum)
            sum=0
data.sort()
print(data[-1]+data[-2]+data[-3])

