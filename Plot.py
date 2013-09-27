import numpy as np
import matplotlib.pyplot as plt
global ax

def set_DrawingArea():
    global ax
    fig, ax = plt.subplots()
    # set ticks and tick labels
    ax.set_xlim(0,100)
    ax.set_xticks(range(0,101,10))
    #ax.set_xticklabels(['0', '$\pi$','2$\pi$'])
    ax.set_ylim(0,100)
    ax.set_yticks(range(0,101,10))


"""
# Only draw spine between the y-ticks
ax.spines['left'].set_bounds(-1, 1)
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
"""

def Draw(x, y):
    global ax
    #plt.clf()
    #x = range(100)
    #y = range(100)
    #y2 = y + 0.1 * np.random.normal(size=x.shape)
    #ax.plot(x, y, 'k--')
    ax.plot(x, y, 'ro')
    plt.show()


if __name__ == '__main__':
    pass