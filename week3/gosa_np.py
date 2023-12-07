import math
import matplotlib.pyplot as plt
import numpy as np

def kaijo(n):
    if n == 0:
        return 1
    elif n > 0:
        return kaijo(n - 1) * n

def my_sin(x, k):
    result = np.zeros_like(x, dtype=float)
    for i in range(0, k):
        index = 2 * i + 1

        mul = x ** index
        sign = 1 if index % 2 == 1 else -1
        dev = kaijo(index)

        result = result + sign * mul / dev

    return result

def gosa(x, k):
    return np.abs(np.sin(x) - my_sin(x, k))

x = np.linspace(0, math.pi, 100)

# マクローリンをk項まで行う
k = 1  

# グラフの設定
y = gosa(x, k)
plt.plot(x, y, label=f'gosa(x), k={k}')

# グラフのタイトル、軸ラベル、凡例の設定
plt.title('Absolute Value Function: gosa(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# グラフの表示
plt.show()
