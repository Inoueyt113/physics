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

# kは項数を表してます。[1,2,3]->[1次,3次,5次]
k_values = [1, 2, 3]

# グラフの設定
for k in k_values:
    y = gosa(x, k)
    plt.plot(x, y, label=f'gosa(x), k={k}')

# グラフのタイトル、軸ラベル、凡例の設定
plt.title('gosa(x) for Various k')
plt.xlabel('x')
plt.ylabel('y')
plt.yscale('log')
plt.legend()

plt.savefig('gosa_plot.png')

# グラフの表示
plt.show()
