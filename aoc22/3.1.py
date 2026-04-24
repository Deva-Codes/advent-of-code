with open ("test.txt",'r') as f:
    sum = 0
    for line in f:
        characters = list(line.strip())
        length = int(len(characters)/2)
        found = False
        for x in range(length):
            if not found:
                for y in range(length,2*length):
                    if characters[x] == characters[y]:
                     print(characters[x])
                     if(ord(characters[x])>90):
                         sum+=ord(characters[x])-96
                     else:
                         sum+=ord(characters[x])-38
                     found = True
                     break
        print("word over")
    print(sum)
       
