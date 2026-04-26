data = []
with open("test.txt",'r') as f:
    for line in f:
            data.append(list(line.strip()))
x =0
sum=0
while(x<len(data)):
      found=False
      for p in data[x]:
            if(found):
                 break
            
            for q in data[x+1]:
                  if(found):
                       break
                  
                  if(p==q):
                        for r in data[x+2]:
                              if found:
                                   break
                              if(q==r):
                                    print(r)
                                    found=True
                                    if(ord(r)>90):
                                     sum+=ord(r)-96
                                    else:
                                      sum+=ord(r)-38
      x+=3
print(sum)
                                    
                  
      