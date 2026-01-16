x = 0
y = 0
aim = 0
with open("test.txt",'r') as f:
    for line in f:
        direction,length  = line.strip().split()
        distance = int(length)
        match direction:
            case 'up':
                
                aim-=distance
            case 'down':
                
                aim+=distance
            case 'forward':
                x+=distance
                y+=aim*distance
               
print(x*y)
