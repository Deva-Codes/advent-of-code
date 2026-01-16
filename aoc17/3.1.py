import math 
def spiral_cordinates(x):
    n = math.ceil((math.sqrt(x)-1)/2)
    
    bottom_right = (2*n+1)**2
    bottom_left =  bottom_right -2*n
    top_left =  bottom_left -2*n
    top_right = top_left-2*n

    if(x>=bottom_left):
            print(-(n-(x-bottom_left)),-n)
    elif(x>=top_left):
            print(-n,-(-n+(x-top_left)))
    elif(x>=top_right):
            print(n-(x-top_right),n)
    else:
            print(n,(x-top_right)+n)
spiral_cordinates(9)
