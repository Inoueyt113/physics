import matplotlib.pyplot as plt
import math as math
k=1
# 勾配場を実数全体で与える関数
def f(x, y):
    return -k * math.sin(x)

# 初期値
x0 = 0.0
y0 = 0.0
v0 = 0.0

# 数値列
x_array_euler = [x0]
y_array_euler = [y0]

x_array_heun = [x0]
y_array_heun = [y0]

# オイラー法による計算
xp = x0
yp = y0
vp = v0
dl = 0.001
for i in range(10000):
    fp = f(xp, yp)
    x_next = xp + dl
    v_next = vp + fp * dl

    x_array_euler.append(x_next)

    fp = v_next
    y_next = yp + fp * dl
    y_array_euler.append(y_next)

    xp = x_next
    yp = y_next
    vp = v_next

# ホイン法による計算
xp = x0
yp = y0
vp = v0
for i in range(10000):
    fp = f(xp, yp)
    x_next = xp + dl
    x_array_heun.append(x_next)

    k1 = fp * dl
    k2 = f(xp + dl, vp + k1) * dl

    v_next = vp + (k1 + k2) / 2

    fp = v_next
    k1 = fp * dl
    k2 = f(vp + dl, yp + k1) * dl

    y_next = yp + (k1 + k2) / 2
    y_array_heun.append(y_next)

    xp = x_next
    yp = y_next
    vp = v_next

# グラフの描画
plt.plot(x_array_euler, y_array_euler, label='Euler Method')
plt.plot(x_array_heun, y_array_heun, label='Heun Method')
plt.title('Euler Method vs Heun Method')
plt.xlabel('time')
plt.ylabel('theta')
plt.legend()
plt.show()
