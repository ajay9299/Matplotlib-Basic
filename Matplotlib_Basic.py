# Basic Funcations Of Matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Line Plot'--------->
'''
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
y = [5,11,12,15,17,19,1,2,3,4,5,6,7,8,9,10,19,20,21,22,1,3,4,5,90,26]
plt.plot(x,y)
plt.title("Random_1")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()
'''
# Line Plot with other parameters
'''
from matplotlib import style # applying Grid on background
style.use("ggplot")
p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
q = [5,11,12,15,17,19,1,2,3,4,5,6,7,8,9,10,19,20,21,22,1,3,4,5,90,26] 
#plt.plot(p,q,color ='y',marker="o", linestyle = "--",markersize = 3)
plt.plot(p,q,"go--",markersize = 3,)  # Direct_Method to apply all in one 
plt.title("Random_2", fontsize = 25)
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.grid(color = "k")
plt.legend("Data")  # We can pass 'loc' parameter in int (0 to 4) for legend position
plt.show()
# We can plot Multipal Lines in one Graph
'''

# Histogram 
import random
'''
Ml_Stu_Age = np.random.randint(12,35,(80))
Py_Stu_Age = np.random.randint(10,25,(80))
plt.hist(Ml_Stu_Age,rwidth=0.8,color= 'm',)
plt.title("Bar_Chart")
plt.xlabel("Ml_Stu_Age")
plt.ylabel("No Of Student")
plt.legend("Bar")
plt.show()
'''
# Two Histrogram In One Graph
'''
from matplotlib import style
style.use("ggplot")
Ml_Stu_Age = np.random.randint(12,35,(80))
Py_Stu_Age = np.random.randint(10,25,(80))
#plt.figure(figsize=(16,9))
plt.hist([Ml_Stu_Age,Py_Stu_Age],color=['m','y'])
#plt.hist(Ml_Stu_Age,rwidth=0.8,color= 'm',)
#plt.hist(Py_Stu_Age,rwidth=0.8,color= 'y',)
plt.title("Bar_Chart")
plt.xlabel("Ml_Stu_Age")
plt.ylabel("No Of Student")
plt.legend("Bar")
plt.show()
'''
# Bar 
'''
# Bar 1st
classes = ['Power_el','Emft','Maths','Hv']
Batch_1 = [10,25,30,15]
Batch_2 = [20,5,40,25]
Batch_3 = [22,45,18,35]
plt.bar(classes,Batch_1)
plt.show()
'''

# Bar 2nd
'''
classes = ['Power_el','Emft','Maths','Hv']
Batch_2 = [20,5,40,25]
plt.bar(classes,Batch_2,align="edge",color ="m",width=0.4) # align , color , width
plt.show()
'''

# Bar 3rd
'''
classes = ['Power_el','Emft','Maths','Hv']
Batch_3 = [22,45,18,35]
plt.bar(classes,Batch_3,linewidth=2,alpha=1,linestyle="--",color ='y',align="edge",width=0.1)
plt.show()
'''

# Overlaping Case In Two Bar
'''
classes = ['Power_el','Emft','Maths','Hv']
Batch_1 = [10,25,30,15]
Batch_2 = [20,5,40,25]
Batch_3 = [22,45,18,35]
plt.bar(classes,Batch_1)
plt.bar(classes,Batch_2,align="edge",color ="m",width=0.4,edgecolor = 'm')
plt.xlabel("Class of Subjects")
plt.ylabel("Students_Numbers")
plt.title("Bar Chart")
plt.show( )
'''
# 3 Bar In One Graph ( vertical)

'''
classes = ['Power_el','Emft','Maths','Hv']
Batch_1 = [10,25,30,15]
Batch_2 = [20,5,40,25]
Batch_3 = [22,45,18,35]
classes_index = np.arange(len(classes))
width = 0.2
plt.bar(classes_index,Batch_1,width=0.2,color ='b')
plt.bar(classes_index + width,Batch_2,color ="g",width=0.2)
plt.bar(classes_index +width +0.2,Batch_3,width=0.2,color="m")
plt.xticks(classes_index+width,classes,rotation = 30)
plt.xlabel("Class of Subjects")
plt.ylabel("Students_Numbers")
plt.title("Bar Chart")
plt.show()
'''
# Horizontal bar problem ?

# Scatters Plot
'''
import random
x = np.random.randint(5,100,(50))
y = np.random.randint(2,200,(50))
#plt.scatter(x,y)
plt.scatter(x,y,c ='r',marker ='*',s = 100,edgecolors='g',linewidths=1) # s = marker_size ,c = scatter_color
plt.show()
'''
# Pie Chart
'''
stu = [30,50,80,40]
clas = ['Hv','Pe','Emft','Opti']
#plt.pie(stu, labels=clas)
explode = [0,0.2,0,0]
color =['r','b','g','y']
textprops = {"fontsize":15}
wedgeprops = {"linewidth":2,"width":1,"edgecolor":'k'}
#plt.pie(stu,labels = clas, explode = explode) # explode use
#plt.pie(stu,labels = clas, explode = explode, autopct="%0.1f%%")  # autopct use
#plt.pie(stu,labels = clas, explode = explode,colors=color, autopct = "%0.1f%%") # color use
#plt.pie(stu,labels = clas, explode = explode,colors=color, autopct = "%0.1f%%", shadow = True) # shaow use
#plt.pie(stu,labels = clas, explode = explode,colors=color, autopct = "%0.1f%%",radius=0.6) # radius use
plt.pie(stu,labels = clas, explode = explode,colors=color, autopct = "%0.1f%%", startangle=90, textprops =textprops)
#plt.pie(stu,labels = clas, explode = explode,colors=color, autopct = "%0.1f%%", startangle=90, textprops =textprops
,pctdistance=0.6,wedgeprops=wedgeprops,rotatelabels = True)
plt.show()
'''
# Subplot
'''
plt.subplot(2,2,1)  # (Row,Coloum,int)    1<= int <=R*C
plt.pie([1])
plt.subplot(2,2,2)
plt.pie([1,2])
plt.subplot(2,2,3)
color = ['k','w','r']
plt.pie([1,2,3],colors=color)
plt.subplot(2,2,4,projection = 'polar',facecolor ='k')
plt.show()
'''
# Savefigure
'''
plt.pie([1,2,3,4])
plt.savefig("NOF",dpi= 100,quality = 99,facecolor = 'y') # dpi = dot per inech
'''


















