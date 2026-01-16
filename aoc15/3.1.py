
visited = {(0,0)}
count=1
with open("test.txt",'r') as f:
   
    for line in f:
        x,y = 0,0
        data = list(line.strip())
      
        for move in data:
         match move:
            case '>':
               x+=1
            case '<':
               x-=1
            case '^':
               y+=1
            case 'v':
              y-=1
         if((x,y) not in visited):
            visited.add((x,y))
            count+=1
print(count)

            
        

            
