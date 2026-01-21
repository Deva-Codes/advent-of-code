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
print(spiral_cordinates(9))
