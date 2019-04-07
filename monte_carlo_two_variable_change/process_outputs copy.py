import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

def into_lists(csv):
    x = csv
    file = open(csv,'r')
    simulation = [[],[],[],[]]
    file.readline()
    for line in file:
        new_line = line.split(',')
        if new_line[2] == '1':
            #creates tuple (coefficiet value, revenue)
            tup = (float(new_line[1]),float(new_line[-1]))
            simulation[0].append(tup)
        elif new_line[2] == '2':
            tup = (float(new_line[1]),float(new_line[-1])) 
            simulation[1].append(tup)
        elif new_line[2] == '14':
            tup = (float(new_line[1]),float(new_line[-1])) 
            simulation[2].append(tup)
        else:
            tup = (float(new_line[1]),float(new_line[-1]))
            simulation[3].append(tup)
    return [x,simulation]

def create_array(return_list):
    for i in range(len(return_list[1])):
        if i == 0:
            title = return_list[0] + ' 1 day simulation'
            to_beat = 439
        elif i == 1:
            title = return_list[0] + ' 2 day simulation'
            to_beat = 2901
        elif i == 2:
            title = return_list[0] + ' 14 day simulation'
            to_beat = 8251 
        else:
            title = return_list[0] + ' 100 day simulation'
            to_beat = 18229
        x = []
        y = []
        for element in return_list[1][i]:
            x.append(element[0])
            y.append(element[1])
        plt.scatter(x,y,label=title)
        #set horizontal line xspan
        number_range = return_list[0]
        number_range = number_range.split()
        rang = number_range[-1]
        rang = rang.strip('(')
        rang = rang.strip(')')
        rang = rang.split(',')
        x1 = float(rang[0])
        x2 = float(rang[1])
        #done setting horizontal line xspan
        w = [x1,x2]
        z = [to_beat,to_beat]
        plt.plot(w,z)
        plt.title(title)
        plt.savefig(title)
        plt.show()

        

            
x = into_lists('monte carlo test line 97 value range step value .5 (0,20)')
create_array(x)



    