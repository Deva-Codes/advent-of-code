def issafe(report):
    safe = True
    num = [int(x) for x in report]
    length  = len(num)
    differences = [num[i] - num[i-1] for i in range(1,length)]
    is_increasing = all(1<=d<=3 for d in differences)
    is_decreasing = all(-3<=d<=-1 for d in differences)
    return is_decreasing or is_increasing

with open("test.txt",'r') as f:
    count=0
    count = sum(1 for line in f if issafe(line.strip().split()))
print(count)

    
