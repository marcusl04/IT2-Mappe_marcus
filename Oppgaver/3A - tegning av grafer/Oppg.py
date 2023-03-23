import matplotlib.pyplot as plt
import numpy as np

3. 
# a)
xverdier = np.linspace(0, 20, 50)
yverdier = 2*xverdier - 3
plt.style.use("seaborn-deep")
plt.plot(xverdier, yverdier)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 20)
plt.ylim(-10, 40)
plt.show()

# b)
xverdier = np.linspace(0, 20, 50)
yverdier = 2*xverdier - 3
plt.plot(xverdier, yverdier, color="skyblue", linewidth=2)
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 20)
plt.ylim(-10, 40)
plt.show()

4. 
xverdier = np.linspace(0, 20, 50)
# Graf 1
yverdier = 0.5*xverdier**2
plt.subplot(1, 2, 1)
plt.plot(xverdier, yverdier)
plt.grid()
# Graf 2
yverdier = -0.3*xverdier**3
plt.subplot(1, 2, 2)
plt.plot(xverdier, yverdier)
plt.grid()
plt.show()

5.
# Graf 1
xverdier = np.linspace(-5, 5, 20)
yverdier = 2*xverdier + 1
plt.subplot(2, 2, 1)
plt.plot(xverdier, yverdier)
plt.grid()
# Graf 2
xverdier = np.linspace(-5, 5, 20)
yverdier = xverdier**2 - 3
plt.subplot(2, 2, 2)
plt.plot(xverdier, yverdier)
plt.grid()
# Graf 3
xverdier = np.linspace(-3, 3, 20)
yverdier = 2**xverdier
plt.subplot(2, 2, 3)
plt.plot(xverdier, yverdier)
plt.grid()
# Graf 4
xverdier = np.linspace(-5, 5, 20)
yverdier = xverdier / 3
plt.subplot(2, 2, 4)
plt.plot(xverdier, yverdier)
plt.grid()
plt.show()

6.