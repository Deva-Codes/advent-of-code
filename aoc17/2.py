with open("test.txt",'r') as f:
    sum=0
    for line in f:
        data=line.strip().split()
        for x in range(len(data)):
            data[x] = int(data[x])
        count=0
        for n in data:
            for d in data:
                if(n%d==0 and n!=d):
                    print(f"{n},{d}")
                    sum+=n/d
                    count+=1
                    break
print(sum)
