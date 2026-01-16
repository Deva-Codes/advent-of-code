data = []
with open("test.txt",'r') as f:
    for line in f:
        data.append(int(line.strip()))
count=0
sums=[]
for x in range(len(data)-2):
    sums.append(data[x]+data[x+1]+data[x+2])
for x in range(1,len(sums)):
    print(sums[x])
    if(sums[x]>sums[x-1]):
        count+=1
print(count)
    
