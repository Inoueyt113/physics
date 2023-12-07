import math
import numpy as np
import matplotlib.pyplot as plt


# time
t_set = 1000000000000
dt = 0.1

# const
rho = 1000
h = 1.73 - 0.2
g = 9.80665

# initial velocity
vx0 = 20
vy0 = 0


def position(d, t_set):
    x_max=0.0
    t_max=0.0

    # initial position    
    x_pos = [0.0]
    y_pos = [h]
    
    r = d / 2
    n = 6 * math.pi * 1.8 * 10 ** -5 * r
    V = (4 * math.pi * r ** 3)/3
    m = V * rho

    steps = int(t_set / dt)
    for i in range(1, steps + 1):
        t = i * dt
        
        x_pos.append(vx0 * math.exp(-n * t / m) * dt + x_pos[i - 1])
        
        
        if math.exp(-n * t / m) == 0.0:
            y_pos.append(-m*g/n)
        else:
            y_pos.append(m * g / n * (math.exp(-n * t / m) - 1) * dt + y_pos[i - 1])
        
        if(y_pos[i] < 0):
            x_max= x_pos[i]
            t_max = t
            break
    
    return x_pos, y_pos, x_max, t_max

# 対数の横軸
d_values = [10**i for i in range(-9, -3)] 
print(d_values)
x_max_values=[]
t_max_values=[]
for d in d_values:
    x,y,x_max,t_max = position(d,t_set)
    x_max_values.append(x_max)
    t_max_values.append(t_max)

print(x_max_values)


# グラフの描画
plt.plot(d_values, x_max_values, markersize=2 ,marker='o', linewidth=1.0)
label = "Projectile Motion (" + str(d) + "m)"
plt.title(label)
plt.xlabel('d(m)')
plt.ylabel('x_max(m)')
plt.xscale('log')  
plt.yscale('log')  
plt.axhline(0, color='black', linewidth=0.1)
plt.axvline(0, color='black', linewidth=0.1)
plt.savefig('xmaxGraph.png')
plt.show()
