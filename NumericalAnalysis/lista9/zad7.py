from data import xs as arguments, ys as values
from nifs3 import get_s
import matplotlib.pyplot as plt

ts_data = [i / 95 for i in range(96)]
sx = get_s(ts_data, arguments)
sy = get_s(ts_data, values)

M = 1000
ui = [i / M for i in range(M)]

plt.plot([sx(u) for u in ui], [sy(u) for u in ui])
plt.show()
