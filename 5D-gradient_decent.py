import time
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

x1 = 7
y1 = 6
z1 = 4
h1 = 2
x2 = -9
y2 = -3
z2 = 4
h2 = 9
x3 = 5
y3 = 7
z3 = -8
h3 = -12


def f(a, b, c, d):
    return a ** 2 / 4 + b ** 2 / 9 + c ** 2 / 16 + d ** 2 / 25


N = 200
delta = 0.01

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(20, 60)

plt.show()
d = 1
point1 = ax.scatter(x1, y1, z1, s=300, c=((1, 0, 0, 1)))
point2 = ax.scatter(x2, y2, z2, s=300, c=((1, 0, 0, 1)))
point3 = ax.scatter(x3, y3, z3, s=300, c=((1, 0, 0, 1)))

mn = 3
for i in range(N):
    lmd = 1 / min(i + 1, mn)
    x1 = x1 - lmd * (f(x1 + delta, y1, z1, h1) - f(x1 - delta, y1, z1, h1)) / (2 * delta)
    x2 = x2 - lmd * (f(x2 + delta, y2, z2, h2) - f(x2 - delta, y2, z2, h2)) / (2 * delta)
    x3 = x3 - lmd * (f(x3 + delta, y3, z3, h3) - f(x3 - delta, y3, z3, h3)) / (2 * delta)

    y1 = y1 - lmd * (f(x1, y1 + delta, z1, h1) - f(x1, y1 - delta, z1, h1)) / (2 * delta)
    y2 = y2 - lmd * (f(x2, y2 + delta, z2, h2) - f(x2, y2 - delta, z2, h2)) / (2 * delta)
    y3 = y3 - lmd * (f(x3, y3 + delta, z3, h3) - f(x3, y3 - delta, z3, h3)) / (2 * delta)

    z1 = z1 - lmd * (f(x1, y1, z1 + delta, h1) - f(x1, y1, z1 - delta, h1)) / (2 * delta)
    z2 = z2 - lmd * (f(x2, y2, z2 + delta, h2) - f(x2, y2, z2 - delta, h2)) / (2 * delta)
    z3 = z3 - lmd * (f(x3, y3, z3 + delta, h3) - f(x3, y3, z3 - delta, h3)) / (2 * delta)

    h1 = h1 - lmd * (f(x1, y1, z1, h1 + delta) - f(x1, y1, z1, h1 - delta)) / (2 * delta)
    h2 = h2 - lmd * (f(x2, y2, z2, h2 + delta) - f(x2, y2, z2, h2 - delta)) / (2 * delta)
    h3 = h3 - lmd * (f(x3, y3, z3, h3 + delta) - f(x3, y3, z3, h3 - delta)) / (2 * delta)

    point1.set_offsets([x1, y1])
    point1.set_3d_properties([z1], 'z')
    point1.set_color(((1 / (1 + np.exp(-(f(x1, y1, z1, h1)))), 0, 0, 1)))
    point1.set_sizes([300*(1 / (1 + np.exp(-(f(x1, y1, z1, h1))))-0.45)])

    point2.set_offsets([x2, y2])
    point2.set_3d_properties([z2], 'z')
    point2.set_color(((1 / (1 + np.exp(-(f(x2, y2, z2, h2)))), 0, 0, 1)))
    point2.set_sizes([300 * (1 / (1 + np.exp(-(f(x1, y1, z1, h1))))-0.45)])

    point3.set_offsets([x3, y3])
    point3.set_3d_properties([z3], 'z')
    point3.set_color(((1 / (1 + np.exp(-(f(x3, y3, z3, h3)))), 0, 0, 1)))
    point3.set_sizes([300 * (1 / (1 + np.exp(-(f(x1, y1, z1, h1))))-0.45)])

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.01)
