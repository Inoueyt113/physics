import matplotlib.pyplot as plt

# 勾配場を実数全体で与える関数
def f(x, y):
    return x

# 初期値
x0 = 0.0
y0 = 0.0

# 数値列
x_array_euler = [x0]
y_array_euler = [y0]

x_array_heun = [x0]
y_array_heun = [y0]

# オイラー法による計算
xp = x0
yp = y0
dl = 0.1
for i in range(100):
    fp = f(xp, yp)
    x_next = xp + dl
    y_next = yp + fp * dl

    x_array_euler.append(x_next)
    y_array_euler.append(y_next)

    xp = x_next
    yp = y_next

# ホイン法による計算
xp = x0
yp = y0
for i in range(100):
    fp = f(xp, yp)
    x_next = xp + dl

    k1 = fp * dl
    k2 = f(xp + dl, yp + k1) * dl

    y_next = yp + (k1 + k2) / 2

    x_array_heun.append(x_next)
    y_array_heun.append(y_next)

    xp = x_next
    yp = y_next

# y=x^2/2 のグラフを追加
x_analytical = x_array_euler  # x軸の値はオイラー法のものを使用
y_analytical = [(x**2)/2 for x in x_analytical]

# グラフの描画
plt.plot(x_array_euler, y_array_euler, label='Euler Method')
plt.plot(x_array_heun, y_array_heun, label='Heun Method')
plt.plot(x_analytical, y_analytical, label='y=x^2/2', linestyle='dashed')
plt.title('Euler Method vs Heun Method with y=x^2/2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
