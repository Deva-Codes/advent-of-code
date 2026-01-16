sum=0
numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
def findnumber(word):
    
    firstfound1=1000
    firstfound2=1000
    firstfound3=1000
    firstfound4=1000
    firstfound1num=1000
    firstfound2num=1000
    firstfound3num=1000
    firstfound4num=1000

    for x in range(len(word)-2):
        temp=word[x:x+3]
        if(temp in numbers):
            firstfound1=x
            firstfound1num=numbers.get(temp)
            break
    for x in range(len(word)-4):
        temp=word[x:x+5]
        if(temp in numbers):
            firstfound2=x
            firstfound2num=numbers.get(temp)
            break
    for x in range(len(word)):
        if(word[x].isdigit()):
            firstfound3=x
            firstfound3num=int(word[x])
            break
    for x in range(len(word)-3):
        temp=word[x:x+4]
        if(temp in numbers):
            firstfound4=x
            firstfound4num=numbers.get(temp)
            break
    secondfound1=-1
    secondfound2=-1
    secondfound3=-1
    secondfound4=-1
    secondfound4num=-1
    secondfound1num=-1
    secondfound2num=-1
    secondfound3num=-1
    for x in range(len(word)-3,-1,-1):
        temp=word[x:x+3]
        if(temp in numbers):
            secondfound1=x
            secondfound1num=numbers.get(temp)
            break
    for x in range(len(word)-4,-1,-1):
        temp=word[x:x+4]
        if(temp in numbers):
            secondfound4=x
            secondfound4num=numbers.get(temp)
            break
            
    for x in range(len(word)-5,-1,-1):
        temp=word[x:x+5]
        if(temp in numbers):
            secondfound2=x
            secondfound2num=numbers.get(temp)
            break
    for x in range(len(word)-1,-1,-1):
        if(word[x].isdigit()):
            secondfound3=x
            secondfound3num=int(word[x])
            break
    firsts = {firstfound1:firstfound1num,firstfound4:firstfound4num,firstfound2:firstfound2num,firstfound3:firstfound3num}
    firstdigit =firsts.get(min(firsts))
    seconds = {secondfound1:secondfound1num,secondfound4:secondfound4num,secondfound2:secondfound2num,secondfound3:secondfound3num}
    seconddigit =seconds.get(max(seconds))
    print(word)
    print(firsts)
    print(seconds)
    print(firstdigit*10+seconddigit)
   
    return(firstdigit*10+seconddigit)


with open("test.txt",'r') as f:
    for line in f:
        data=(line.strip())
        sum+=findnumber(data)
print(sum)

#optimised code
numbers = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0
}

def findnumber(word):
    digits_found = []

    for i in range(len(word)):
        # Check for literal digits
        if word[i].isdigit():
            digits_found.append(int(word[i]))
        
        # Check for spelled-out digits
        for name, val in numbers.items():
            if word[i:].startswith(name):
                digits_found.append(val)

    if not digits_found:
        return 0
        
    # Combine first and last digit found
    return (digits_found[0] * 10) + digits_found[-1]

# Main execution
total_sum = 0
with open("test.txt", 'r') as f:
    for line in f:
        total_sum += findnumber(line.strip())

print(total_sum)

  