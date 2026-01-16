sum=0
with open("test.txt",'r') as f:
    for line in f:
        dimensions = [int(x) for x in line.strip().split('x')]
        dimensions.sort()
        product =1
        for dimension in dimensions:
            product*=dimension
        sum+= product+2*(dimensions[1]+dimensions[0])
print(sum)