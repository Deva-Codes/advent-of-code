def issafe(num):
    safe = True
    length  = len(num)
    differences = [num[i] - num[i-1] for i in range(1,length)]
    is_increasing = all(1<=d<=3 for d in differences)
    is_decreasing = all(-3<=d<=-1 for d in differences)
    return is_decreasing or is_increasing
def really_safe(report):
    
    for i in range(len(report)):
        num = report[0:i]+report[i+1:]
        if(issafe(num)):
            return True
    return False
           
    

with open("test.txt",'r') as f:
    count=0
    for line in f:
        report =[int(x) for x in   line.strip().split()]
        if issafe(report) or really_safe(report):
            count+=1


print(count)

    
