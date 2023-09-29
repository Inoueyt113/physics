import math
import numpy as np
import matplotlib.pyplot as plt



t_max=250
dt = 0.1
rho = 1000
n = 1.8 * 10 ** 3
h = 1.73 - 0.2 
vx0 = 20
vy0 = 0
g = 9.80665

x_pos = [0.0]
y_pos = [h]

def position(d, t_max):
    r = d/2
    V = 4/3 * math.pi * r ** 3
    m = V * rho

    print(m,n,dt)


    steps = int(t_max / dt)
    print(steps)
    for i in range(1, steps):
        t= i * dt
        x_pos.append( vx0 * math.exp(-n*t /m) *dt + x_pos[i-1] )
        y_pos.append(m*g/n * (math.exp(-n*t/m ) - 1) *dt + y_pos[i-1] )


d= 0.01
position(d, t_max)
# print(x_pos)
# print(y_pos)

# グラフの描画
plt.plot(x_pos, y_pos, marker='o', linewidth=1.0)
plt.title('Projectile Motion')
plt.xlabel('X Position(m)')
plt.ylabel('Y Position(m)')
plt.axis('equal')
plt.axhline(0, color='black', linewidth=0.1)
plt.axvline(0, color='black', linewidth=0.1)
plt.show()
    
