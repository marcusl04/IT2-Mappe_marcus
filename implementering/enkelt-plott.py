import matplotlib.pyplot as plt

# x = [0, 1, 2, 3, 4, 5]
# y = [2, 5, 8, 11, 14, 17]

# plt.plot(x, y) # oppretter et plot
# plt.show() # viser plottet

x = []

y = []

for i in range(6):
    x.append(i)
    y.append(3*1 + 2)

plt.plot(x, y)
plt.show()