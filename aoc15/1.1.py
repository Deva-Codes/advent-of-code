with open("test.txt", 'r') as f:
    data = f.read()
    floor = data.count('(') - data.count(')')

print(floor)