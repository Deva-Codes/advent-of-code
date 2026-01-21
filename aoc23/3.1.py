import re
data = []
sum = 0
with open("test.txt",'r') as f:
    data = [line.strip() for line in f]
rows = len(data)
columns = len(data[0])
def valid(r,start_position,end_position):
   start_r = max(0,r-1)
   end_r = min(rows,r+2)
   start_c = max(0,start_position-1) 
   end_c = min(columns,end_position+1)
   is_valid = False
   for x in range(start_r,end_r):
       for y in range(start_c,end_c):
           element = data[x][y]
           if not element.isdigit() and element != '.':
               is_valid = True
               return is_valid
               break
       if is_valid:
               break         
for r , row in enumerate(data):
    for match in re.finditer(r"\d+",row):
        number = int(match.group())
        start_position = match.start()
        end_position = match.end()
        if(valid(r,start_position,end_position)):
            sum+=number
print(sum)




