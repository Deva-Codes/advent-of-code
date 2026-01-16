sum=0
with open("test.txt",'r') as f:
    for line in f:
        l,b,h = [int(x) for x in line.strip().split('x')]
        sum+=2*(l*b+b*h+l*h)+min(l*b,b*h,l*h)
print(sum)