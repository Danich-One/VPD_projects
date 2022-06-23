import time
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

'''def f(x):
    return np.sin(x)+0.5*x

x_plt = np.arange(-5, 5, 0.1)
y_plt = [f(x) for x in x_plt]

plt.xlabel('x')
plt.ylabel('y')

x1 = 3
x2 = -4
x3 = 2
N = 200
delta = 0.01

plt.ion()
fig, ax = plt.subplots()
ax.grid(True)

ax.plot(x_plt, y_plt)
point1 = ax.scatter(x1, f(x1), c='red')
point2 = ax.scatter(x2, f(x2), c='red')
point3 = ax.scatter(x3, f(x3), c='red')


mn = 10
for i in range(N):
    lmd = 1/min(i+1, mn)
    x1 = x1 - lmd*(f(x1+delta)-f(x1-delta))/(2*delta)
    x2 = x2 - lmd*(f(x2+delta)-f(x2-delta))/(2*delta)
    x3 = x3 - lmd*(f(x3+delta)-f(x3-delta))/(2*delta)
    point1.set_offsets([x1, f(x1)])
    point2.set_offsets([x2, f(x2)])
    point3.set_offsets([x3, f(x3)])
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)'''

'''plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c='blue')
plt.show()'''

def f(a, b):
    return a**2/4+b**2/9

x_plt = np.arange(-5, 5, 0.1)
y_plt = np.arange(-5, 5, 0.1)
x_plt, y_plt = np.meshgrid(x_plt, y_plt)
z_plt = x_plt**2/4 + y_plt**2/9

x1 = 7
y1 = 6
x2 = -9
y2 = -3
x3 = 5
y3 = -7
N = 200
delta = 0.01

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(20, 60)

ax.plot_surface(x_plt, y_plt, z_plt, color='b', alpha = 0.5)

plt.show()
d = 1
point1 = ax.scatter(x1, y1, f(x1, y1)+d, c='red')
point2 = ax.scatter(x2, y2, f(x2, y2)+d, c='red')
point3 = ax.scatter(x3, y3, f(x3, y3)+d, c='red')


mn = 5
for i in range(N):
    lmd = 1/min(i+1, mn)
    x1 = x1 - lmd*(f(x1+delta,y1)-f(x1-delta, y1))/(2*delta)
    x2 = x2 - lmd*(f(x2+delta, y2)-f(x2-delta, y2))/(2*delta)
    x3 = x3 - lmd*(f(x3+delta, y3)-f(x3-delta, y3))/(2*delta)
    y1 = y1 - lmd * (f(y1 + delta, x1) - f(y1 - delta, x1)) / (2 * delta)
    y2 = y2 - lmd * (f(y2 + delta, x2) - f(y2 - delta, x2)) / (2 * delta)
    y3 = y3 - lmd * (f(y3 + delta, x3) - f(y3 - delta, x3)) / (2 * delta)
    point1.set_offsets([x1, y1])
    point1.set_3d_properties([f(x1, y1)+d],'z')
    point2.set_offsets([x2, y2])
    point2.set_3d_properties([f(x2, y2) + d], 'z')
    point3.set_offsets([x3, y3])
    point3.set_3d_properties([f(x3, y3) + d], 'z')
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.01)