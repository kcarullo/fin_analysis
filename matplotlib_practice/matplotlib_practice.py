import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

# Functional method
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.plot()

plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')

# object oriented 
fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')


# index 0 is location for width, 1 is location for height, 2 how wide the figure is
# 3 is the height of the figure 
fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.3,0.3])

axes1.plot(x,y)
axes1.set_title('LARGER PLOT')
axes2.plot(y,x)
axes2.set_title('smaller plot')