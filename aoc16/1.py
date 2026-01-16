x=0
y=0
direction =0 

def getcordinate(move):
    global x,y,direction
    if(move[0]=='R'):
        if(direction==0):
            direction =1
            x+=int(move[1:])
        elif(direction==1):
            direction =2
            y-=int(move[1:])
        elif(direction==2):
            direction=3
            x-=int(move[1:])
        else:
            direction=0
            y+=int(move[1:])
                 
    else:
        if(direction==0):
            direction =3
            x-=int(move[1:])

        elif(direction==1):
            direction=0
            y+=int(move[1:])
        elif(direction==2):
            x+=int(move[1:])
            direction=1
        else:
            direction=2
            y-=int(move[1:])
    return[x,y]
def storecordinates(beforemove,aftermove):
    global cordinates
    if(abs(beforemove[0]-aftermove[0])!=0):
       if(aftermove[0]>beforemove[0]):
           for i in range(beforemove[0]+1,aftermove[0]+1):
               if([i,beforemove[1]] in cordinates):
                   print(f"element found{i,beforemove[1]}")
                   break
               else:
                   cordinates.append([i,beforemove[1]])
       else:
           for i in range(beforemove[0]-1,aftermove[0]-1,-1):
               if([i,beforemove[1]] in cordinates):
                   print(f"element found{i,beforemove[1]}")
                   break
               else:
                   cordinates.append([i,beforemove[1]])
           
    else:
        if(aftermove[1]>beforemove[1]):
           for i in range(beforemove[1]+1,aftermove[1]+1):
               if([beforemove[0],i] in cordinates):
                   print(f"element found{beforemove[0],i}")
                   break
               else:
                   cordinates.append([beforemove[0],i])
        else:
           for i in range(beforemove[1]-1,aftermove[1]-1,-1):
               if([beforemove[0],i] in cordinates):
                   print(f"element found{beforemove[0],i}")
                   break
               else:
                   cordinates.append([beforemove[0],i])
    
cordinates = [[0,0]]
data=[]
with open("test.txt",'r') as f:
    for line in f:
        data=line.split(',')
for element in data:
   move= element.strip()
   beforemove = [x,y]
   aftermove=getcordinate(move)
   storecordinates(beforemove,aftermove)

