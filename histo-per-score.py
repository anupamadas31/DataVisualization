from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import numpy as np
from sklearn.metrics import accuracy_score

# df =pd.read_csv(r'/media/anapuma/My Passport/CARINATA/phase2/inputfiles/input.csv')
df =pd.read_csv(r'D:/CARINATA/phase2/inputfiles/classwise_vardist.csv')
df1=df[[0,1,2]]
df2=df[[3,4,5]]

data7=df.iloc[:,[0,1,2]].values
flat_list7 = [item for sublist in data7 for item in sublist]
min7=min(flat_list7)
max7=max(flat_list7)
binwidth7=(max7-min7)/20


data19=df.iloc[:,[3,4,5]].values
flat_list19 = [item for sublist in data19 for item in sublist]
min19=min(flat_list19)
max19=max(flat_list19)
binwidth19=(max19-min19)/20

####stacked histo######
# binwidth=(data.max()-data.min())/20
# min=data.min()
# max=data.max()+binwidth
# plt.hist(data, bins=np.arange(min,max, binwidth),stacked=True,color=['red','blue','yellow'],
#                           label=['class1', 'class2','class3'])

#####line plot####
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot(df1)
plt.title('7june')
plt.subplot(212)             # the second subplot in the first figure
plt.plot(df2)
plt.legend(['class1', 'class2','class3'])
plt.xlabel('count')
plt.ylabel('variance of distances from crop rowline')
plt.title(' 19june')
plt.show()



#########side by side histo#######
a=df.iloc[:,[0]].values
b=df.iloc[:,[1]].values
c=df.iloc[:,[2]].values
d=df.iloc[:,[3]].values
e=df.iloc[:,[4]].values
f=df.iloc[:,[5]].values
common_params7 = dict(bins=(np.arange(min7,max7, binwidth7)),range=(min7,max7),
                            label=['class1', 'class2','class3'])
common_params19= dict(bins=(np.arange(min19,max19, binwidth19)),range=(min19,max19),
                            label=['class1', 'class2','class3'])

plt.subplot(211)
plt.title('7june')
plt.hist((a, b, c), **common_params7)
plt.legend()
plt.subplot(212)
plt.title('19june')
plt.hist((d,e,f), **common_params19)
plt.xlabel('variance of distances from crop rowline')
plt.ylabel('count')
plt.legend()
plt.show()



##########stack area plot########

plt.title('7june')
df1.plot.area()
plt.xlabel('count')
plt.ylabel('variance of distances from crop rowline')
plt.show()

plt.title('19june')
df2.plot.area()
plt.xlabel('count')
plt.ylabel('variance of distances from crop rowline')
plt.show()




