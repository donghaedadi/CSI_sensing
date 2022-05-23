from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import matplotlib
import time
#
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
from socket import *
import time
from matplotlib.animation import FuncAnimation

class SocketInfo():
    HOST=""
    PORT=8888
    BUFSIZE=7
    ADDR=(HOST, PORT)

class socketInfo(SocketInfo):
    HOST = "127.0.0.1"

csock = socket(AF_INET, SOCK_STREAM)
csock.connect(socketInfo.ADDR)
print("conenct is success")

x = np.linspace(0, 10, 100)
y = np.cos(x) * 10
new_y = y

plt.ion()

figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot(x, y)

plt.title("random grahp show",fontsize=25)
plt.xlabel("X",fontsize=18)
plt.ylabel("radomdata",fontsize=18)

# while True:
for r in range(100):
    commend = csock.recv(socketInfo.BUFSIZE, MSG_WAITALL)
    data = commend.decode("UTF-8")
    data_int = 10
    print("type : {}, data len : {}, data : {}, Contents : {}".format(type(commend),len(commend), commend, data))

    data_int = int(data[0])
    print(type(data_int))

    line1.set_xdata(x)
    line1.set_ydata(new_y)

    r = data_int
    old_y = line1.get_ydata()
    new_y = np.r_[old_y[1:], r]

    figure.canvas.draw()    
    figure.canvas.flush_events()
    time.sleep(0.1)


    # figure.canvas.draw.save(r'animation.gif', fps=10)


    # x = []
    # y = []

    # figure, ax = plt.subplots(figsize=(4,3))
    # line, = ax.plot(x, y)
    # plt.axis([0, 4*np.pi, -1, 1])
    # r = data_int

    # def func_animate(i):
    #     x = np.linspace(0, 4*np.pi, 1000)
    #     old_y = line1.get_ydata()
    #     y = np.r_[old_y[1:], r]
    
    #     line.set_data(x, y)
    #     return line,

    # ani = FuncAnimation(figure,
    #                 func_animate,
    #                 frames=10,
    #                 interval=50)

    # ani.save(r'animation.gif', fps=10)

    # plt.show()
    # for i  in range(10):
    #     x = x + 0.1
    #     y = data

    #     plt.scatter(x, y)
    #     plt.pause(0.1)
    #     plt.show

    
    # fig = plt.figure()     #figure(도표) 생성
    # ax = plt.subplot(211, xlim=(0, 50), ylim=(0, 1024))
    # max_points = 50
    # line, = ax.plot(np.arange(max_points), 
    #            np.ones(max_points, dtype=float)*np.nan, lw=1, c='blue',ms=1)
    # def init():
    #  return line

    # def animate(i):
#       y = data
#       old_y = line.get_ydata()
#       new_y = np.r_[old_y[1:], y]
#       line.set_ydata(new_y)
#       print(new_y)
#       return line

#     root = Tk.Tk() #추가
#     label = Tk.Label(root,text="라벨").grid(column=0, row=0)#추가
#     canvas = FigureCanvasTkAgg(fig, master=root) #
#     canvas.get_tk_widget().grid(column=0,row=1) #

#     anim = animation.FuncAnimation(fig, animate  , init_func= init ,frames=200, interval=50, blit=False)
#     Tk.mainloop()

# csock.close()
# exit()
