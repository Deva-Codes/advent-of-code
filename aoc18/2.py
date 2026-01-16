import sys
data = []

count=0
with open("test.txt",'r') as f:
    for line in f:
        data.append(list(line.strip()))
for x in range(len(data)):
    for y in range(x,len(data)):

        if(x!=y and len(data[x]) == len(data[y])):
            count=0
            for p in range(len(data[x])):
                if(data[x][p]!=data[y][p]):
                    
                    count+=1
           
        if(count==1):
         for element in data[x]:
             print(element,end='')
         print()
         for element in data[y]:
             print(element,end = '')

         sys.exit()

        
            
