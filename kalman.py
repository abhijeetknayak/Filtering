import numpy as np
import matplotlib.pyplot as plt

z_obs = np.random.randn(100)
x = np.linspace(1, 100, 100)
plt.plot(x, z_obs, 'b')
pred = 0.0
xFinal = []

for i in range(len(z_obs)):
    if i == 0:
        r = 0
    else:
        r = abs(z_obs[i] - z_obs[i - 1]) / 10
    kalmanGain = 0.1 / (0.1 + r)

    xFinal.append(pred + kalmanGain * (z_obs[i] - pred))

plt.plot(x, xFinal, 'g')

plt.show()