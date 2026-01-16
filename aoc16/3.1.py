count=0
with open("test.txt",'r') as f:
    for line in f:
        x,y,z = [int(x) for x in line.strip().split()]
        if x+y>z and x+z>y and y+z>x:
            count+=1
print(f"there are {count} valid triangles")