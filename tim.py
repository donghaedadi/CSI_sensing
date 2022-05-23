# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# x = []
# y = []

# figure, ax = plt.subplots(figsize=(4,3))
# line, = ax.plot(x, y)
# plt.axis([0, 4*np.pi, -1, 1])

# def func_animate(i):
#     x = np.linspace(0, 4*np.pi, 1000)
#     y = np.sin(2 * (x - 0.1 * i))
    
#     line.set_data(x, y)
    
#     return line,

# ani = FuncAnimation(figure,
#                     func_animate,
#                     frames=10,
#                     interval=50)

# ani.save(r'animation.gif', fps=10)

# plt.show()


# //////////////////////////////////////////////////////////
import numpy as np
import time
import matplotlib.pyplot as plt
import random 

x = np.linspace(0, 10, 100)
y = np.cos(x) * 10
new_y = y

plt.ion()

figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot(x, y)

plt.title("random grahp show",fontsize=25)
plt.xlabel("X",fontsize=18)
plt.ylabel("radomdata",fontsize=18)

while True:    
    line1.set_xdata(x)
    line1.set_ydata(new_y)

    r = random.randint(0, 1)
    old_y = line1.get_ydata()
    new_y = np.r_[old_y[1:], r]

    figure.canvas.draw()    
    figure.canvas.flush_events()
    time.sleep(0.1)

    

#///////////////////////////////////////////////////////////
# import numpy as np
# import matplotlib.pyplot as plt

# x = 0
# while True:
#     for i in range(10):
#         x = x +0.1
#         y = np.sin(x)

#         plt.scatter(x,y)
#         plt.pause(0.001)
#     plt.show
#     #x = x-1