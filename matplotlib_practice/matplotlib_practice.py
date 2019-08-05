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


fig, axes = plt.subplots(nrows=1,ncols=2)
for current_ax in axes:
    current_ax.plot(x,y)
    
fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')

plt.tight_layout()

# Figure Size and DPI(dots per inch)
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))

axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()

fig.savefig('my_picture.png', dpi=100)

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label='X Squared')
ax.plot(x, x**3, label='X Cubed')

#loc or location places legend where you want to put it, 0 is best fit
ax.legend(loc=0)

# setting colors 
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color='green', lw=3, linestyle='--', marker='*', markersize=20, markerfacecolor='blue', markeredgewidth=3, markeredgecolor='yellow')  

# zooms into a specific portion of the chart
#ax.set_xlim([0,1])
#ax.set_ylim([0,2])

# look up RGB hex color

plt.show() 
