import math
import numpy as np
import matplotlib.pyplot as plt

d=0.0001


t_set = 1000
dt = 0.01
rho = 1000
r = d / 2
n = 6 * math.pi * 1.8 * 10 ** -5 * r
h = 1.73 - 0.2
vx0 = 20
vy0 = 0
g = 9.80665
V = (4 * math.pi * r ** 3)/3
m = V * rho

# x_pos = [0.0]
# y_pos = [h]


def position(d, t_set):
    x_max=0.0
    t_max=0.0
    x_pos = [0.0]
    y_pos = [h]


    steps = int(t_set / dt)
    for i in range(1, steps + 1):
        t = i * dt
        # print(math.exp(-n * t / m)-1)
        x_pos.append(vx0 * math.exp(-n * t / m) * dt + x_pos[i - 1])
        y_pos.append(m * g / n * (math.exp(-n * t / m) - 1) * dt + y_pos[i - 1])
        if(y_pos[i] < 0):
            x_max= x_pos[i]
            t_max = t
            break
    
    return x_pos, y_pos, x_max, t_max

# 対数の横軸
# d_values = [10**i for i in range(-6, 0)] 
# d_values = np.logspace(-6, 0, num=100)
# x_max_values=[]
# y_max_values=[]
# for d in d_values:
#     x,y,x_max,y_max = position(d,t_set)
#     x_max_values.append(x_max)
#     y_max_values.append(y_max)

x_pos, y_pos,x_max,t_max= position(d, t_set)

# グラフの描画
plt.plot(x_pos, y_pos, markersize=2 ,marker='o', linewidth=1.0)
print(t_max)
label = "Projectile Motion (" + str(d) + "m) " + str(t_max) + "s"
plt.title(label)
plt.xlabel('X Position(m)')
plt.ylabel('Y Position(m)')
plt.axis('equal')
plt.axhline(0, color='black', linewidth=0.1)
plt.axvline(0, color='black', linewidth=0.1)
plt.savefig('PM.png')
plt.show()
