move = {'>':(1,0),'<':(-1,0),'^':(0,1),'v':(0,-1)}
sx,sy = 0,0
rx,ry= 0,0
visited = {(0,0)}
with open("test.txt",'r') as f:
    for line in f:
        map = list(line.strip())
    for x in range(len(map)):
        dx,dy = move[map[x]]
        if(x%2==0):
            sx+=dx;sy+=dy
            visited.add((sx,sy))
        else:
            rx+=dx;ry+=dy
            visited.add((rx,ry))
print(len(visited))


