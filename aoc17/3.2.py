import math 
def spiral_cordinates(x):
    n = math.ceil((math.sqrt(x)-1)/2)
    
    bottom_right = (2*n+1)**2
    bottom_left =  bottom_right -2*n
    top_left =  bottom_left -2*n
    top_right = top_left-2*n

    if(x>=bottom_left):
            return(-(n-(x-bottom_left)),-n)
    elif(x>=top_left):
            return(-n,-(-n+(x-top_left)))
    elif(x>=top_right):
            return(n-(x-top_right),n)
    else:
            return(n,(x-top_right)+n)
def find_sum_number(p):
    data_set = {(0,0):1}
    initial =1
    while 1:
        sum=0
        initial+=1
        current = spiral_cordinates(initial)
        for x in [-1,0,1]:
               for y in [-1,0,1]:
                      if(x==0 and y==0):
                             continue
                      sum+=data_set.get((current[0]+x,current[1]+y),0)

        if(sum>p) :
              #  print(data_set)
                return(sum)
        else:
                data_set[current] = sum
               
print(find_sum_number(368078))

       


