keypad = [['0','0','1','0','0'],['0','2','3','4','0'],['5','6','7','8','9'],['0','A','B','C','0'],['0','0','D','0','0']]
location = [2,0]

def findnum(data):
    global location
    for move in data:
        if(move=='U'):
            if(location[0]>0 ):
             if(keypad[location[0]-1][location[1]]!='0'):
              location[0]-=1
            
        elif(move=='D' ):
            if(location[0]<4):
             if( keypad[location[0]+1][location[1]]!='0'):
              location[0]+=1
            
        elif(move=='R'):
            if(location[1]<4 ):
                if( keypad[location[0]][location[1]+1]!='0'):
                  location[1]+=1     
        else:
            if(location[1]>0 ):
                if( keypad[location[0]][location[1]-1]!='0'):
                 location[1]-=1
    print(location,data)
    return(keypad[location[0]][location[1]])
num=''
with open("test.txt",'r') as f:
    for line in f:
        data=list(line.strip())
        num+=findnum(data)
       
print(num)