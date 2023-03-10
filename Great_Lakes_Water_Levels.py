<<<<<<< HEAD
=======
""""
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 

>>>>>>> hanhoupu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years



# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years

# +
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sup.csv')

plt.plot(df['year'],df['lake levels'])
# -


# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

data = pd.read_csv('eri.csv')
plt.plot(data['time'],data['water level'])
plt.xlabel('Time (Years)')
plt.ylabel('Water Level')
plt.title('Lake Erie')

# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years
ont = pd.read_csv("ont.csv")
x = ont.iloc[:,0]
y = ont.iloc[:,1]
plt.plot(x,y)
plt.xlabel("Year")
plt.ylabel("Ontario Water Level")
plt.title("Ontario Water Level as a function of time years")



# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.



# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.



# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


