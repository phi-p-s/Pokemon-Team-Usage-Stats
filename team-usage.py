import sys
"""
To call: python3 .\\team-usage.py {usage.txt} mon1 ... mon6
"""
def read_file(filename):
    #open file
    f = open(filename, 'r')
    #get total battles (idk if this important)
    n = f.readline()
    n = n.split()
    n = int(n[-1])
    clean_lines = {}
    #read file
    for line in f:
        #cleaning their formatting and making a list
        temp = line.replace('|', '')
        temp = temp.replace('+', '')
        temp = temp.replace('-', '')
        temp = temp.split()
        #check to make sure its a mon (They start with a rank)
        if len(temp) > 0:
            if temp[0].isnumeric():
                #create dictionary with pokemon name as key
                name = temp[1]
                temp.pop(1)
                clean_lines.update({name: temp})
    f.close()
    #checking clean_lines
    '''
    for line in clean_lines:
        print(line)
    '''
    #Key: Name ----- 0-Rank 1-Use% 2-#Raw 3-Raw% 4-#Real 5-Real%
    #Use% - Weighted, has an elo cutoff
    #Raw - Total games in general
    #Real - Games where the mon appeared (Leftover from no team preview essentially)
    return clean_lines, n

def use_percent(mon, usage_dict):
    percentage = usage_dict[mon][1]
    #turn into float
    percentage = float(percentage.replace("%", ""))
    return percentage

#n, number 1-6
#mons, names of mons dict
def use_avg_team(n, mons, usage_dict):
    avg = 0
    for i in range(n):
        weight = (1/n)
        usage = use_percent(mons[i], usage_dict)
        avg += (weight)*usage
        print("Mon: " + str(mons[i]))
        print("Usage: " + str(usage))
    print(avg)

#if no arguments, just use these
if len(sys.argv) == 1:
    usage_dict, n = read_file("feb-2023-dou.txt")
    mons = ["IndeedeeF", "Armarouge", "Maushold", "Annihilape", "Amoonguss", "Torkoal"]
#too many arguments (Max 8. 1 Default, 1 For usage sheet, 6 for mons)
elif len(sys.argv) > 8:
    print("Too many arguments", file=sys.stderr)
    exit(1)
elif len(sys.argv) == 2:
    usage_dict, n = read_file(sys.argv[1])
    mons = ["IndeedeeF", "Armarouge", "Maushold", "Annihilape", "Amoonguss", "Torkoal"]
else:
    usage_dict, n = read_file(sys.argv[1])
    mons = []
    for i in range(2, len(sys.argv)):
        mons.append(sys.argv[i])

use_avg_team(len(mons), mons, usage_dict)