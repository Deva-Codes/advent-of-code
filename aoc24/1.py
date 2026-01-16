firsts = []
seconds = []
with open("test.txt",'r') as f:
    for line in f:
        data=line.strip().split()
        firsts.append(int(data[0]))
        seconds.append(int(data[1]))
firsts.sort()
seconds.sort()
sum=0
for x in range(len(firsts)):
    count=0
    for y in range(len(firsts)):
        if(seconds[y]>firsts[x]):
            break
        else:
            if(firsts[x]==seconds[y]):
                count+=1
    sum+=firsts[x]*count
print(sum)

