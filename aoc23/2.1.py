"""""
count=0
with open ("test.txt",'r') as f:
    for line in f:
        mr=0
        mg=0
        mb=0
        game = line.strip().split(':')
        sets =game[1].split(';')
        
        for set in sets:
            set=set.split(',')
            for subset in set:
                subset = subset.strip().split(' ')
                match subset[1]:
                    case 'blue':
                        if(int(subset[0])>mb):
                            mb = int(subset[0])
                    case 'red':
                        if(int(subset[0])>mr):
                            mr = int(subset[0])
                    case 'green':
                        if(int(subset[0])>mg):
                            mg = int(subset[0])
        if(mb<=14 and mg<=13 and mr<=12):
            
            count+=int(game[0].split(' ')[1])
print(count)
"""""
count=0
color_limits = {"red":12,"blue":14,"green":13}
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
                if(max_color[cube_color]>color_limits[cube_color]):
                    possible = False
                    break
        if possible:count+=int(game.strip().split()[1])
print(count)


       