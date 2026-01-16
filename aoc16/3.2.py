matrix = []
count=0
def valid(x,y,z):
    return  x+y>z and x+z>y and y+z>x
         
with open("test.txt",'r') as f:
    for line in f:
        matrix.append([int(x) for x in line.strip().split()])
for i in range(0,len(matrix),3):
    for j in range(3):
        x,y,z = matrix[i][j],matrix[i+1][j],matrix[i+2][j]
        if valid(x,y,z):
            count+=1
print(count)
        
