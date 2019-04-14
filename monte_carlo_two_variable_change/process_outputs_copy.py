import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
import pandas as pd 
import numpy as np 

def into_lists(csv):
    x = csv
    file = open(csv,'r')
    simulation = [[],[],[],[]]
    file.readline()
    for line in file:
        new_line = line.split(',')
        if new_line[3] == '1':
            #creates tuple (coefficiet value, revenue)
            tup = ((float(new_line[2]),float(new_line[1])),float(new_line[-1]))
            simulation[0].append(tup)
        elif new_line[3] == '2':
            tup = ((float(new_line[2]),float(new_line[1])),float(new_line[-1])) 
            simulation[1].append(tup)
        elif new_line[3] == '14':
            tup = ((float(new_line[2]),float(new_line[1])),float(new_line[-1])) 
            simulation[2].append(tup)
        else:
            tup = ((float(new_line[2]),float(new_line[1])), float(new_line[-1]))
            simulation[3].append(tup)
    return [x,simulation]

def create_array(return_list):
    for i in range(4): #iterates through big list containing 4 lists corresponding to simulation
        #these booleans identify the simulation title
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
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
        #creates plots
        x = []
        y = []
        z = []
        big_list = return_list[1]
        for element in big_list[i]:
            x.append(element[0][0])
            y.append(element[0][1])
            z.append(element[1])
        ax.scatter(x, y, z)
        plt.title(title)
        plt.ylabel('days value')
        plt.xlabel('demand value')
        #if i == 3:
        #    plt.savefig('v1=(dl>12) v2=(150<demand<200), 100 day simulation')
        plt.show()

x=into_lists('v1=(dl>12) v2=(150<demand<200).csv')
create_array(x)

def create_graph(return_list):
    for i in range(len(return_list[1])):
        if i == 0:
            title = return_list[0] + ' 1 day simulation'
            to_beat = 439
            rev = return_list[-1]
        elif i == 1:
            title = return_list[0] + ' 2 day simulation'
            to_beat = 2901
            rev = return_list[-1]
        elif i == 2:
            title = return_list[0] + ' 14 day simulation'
            to_beat = 8251 
            rev = return_list[-1]
        else:
            title = return_list[0] + ' 100 day simulation'
            to_beat = 18229
            rev = return_list[-1]
        x=[]
        y=[]
        z=[]
        for item in return_list[1][i]:
            x.append(item[0])
            y.append(item[1])
            z.append(item[-1])
        graph = plt.figure()
        ax = graph.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, zdir='z')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        #set horizontal line xspan
        #number_range = return_list[0]
        #number_range = number_range.split()
        #rang = number_range[-1]
        #rang = rang.strip('(')
        #rang = rang.strip(')')
        #rang = rang.split(',')
        #x1 = float(rang[0])
        #x2 = float(rang[1])
        #done setting horizontal line xspan
        #w = [x1,x2]
        #y_pt = [to_beat,to_beat]
        #z_pt= [rev,rev]
        #plt.plot(w,y_pt,z_pt)
        #plt.title(title)
        plt.savefig(title)
        plt.show()





        

            
# x = into_lists('monte carlo test line 97 value range step value .5 (0,20)')
# create_array(x)



    