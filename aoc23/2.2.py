sum=0
with open("test.txt",'r') as f:
    for line in f:
        possible= True
        game,game_data =line.strip().split(':')
        max_color = {"red":0,"blue":0,"green":0}
        pulls = game_data.strip().replace(';',',').split(',')
        for pull in pulls:
            cube_count,cube_color = pull.strip().split()
            cube_num = int(cube_count)
            if(cube_num>max_color[cube_color]):
                max_color[cube_color]=cube_num
        sum+=max_color['blue']*max_color['red']*max_color['green']
print(sum)