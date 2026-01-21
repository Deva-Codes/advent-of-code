visited = set()
already_visited = set()
count=0
with open("test.txt",'r') as f:
    for line in f:
        line_data = line.strip().split()
        i,j = [int(x) for x in line_data[2][0:-1].split(",")]
        h,v = [int(x) for x in line_data[3].split('x')]
        for x in range(i,i+h+1):
            for y in range(j,j+v+1):
                print(x,y)
                if(x,y) in visited and (x,y) not in already_visited :
                    count+=1
                    already_visited.add((x,y))
                else:
                    visited.add((x,y))
print(count)

        
        
        


    