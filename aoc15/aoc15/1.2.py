move = {')':-1,'(':1}
floor =0
with open("test.txt",'r') as f:
    for line in f:
        data = line.strip()
        for x in range(len(data)):
            floor+= move[data[x]]
            if floor<0:
                print(x+1)
                break
