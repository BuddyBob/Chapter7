import numpy as np
import matplotlib.pyplot as plt

L = 1
k = 1
A = 3

t = np.linspace(-6, 10, 400)
y = L / (1 + A * np.exp(-k * t))

plt.figure(figsize=(8,5))
plt.plot(t, y, linewidth=2)
plt.axhline(L, linestyle='--', color='gray', linewidth=1)
plt.text(-5.5, 1.05, 'Carrying capacity (L)', va='bottom')
plt.title('Standard Logistic Curve')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.tight_layout()

file_path = "logistic_curve_example1.png"
plt.savefig(file_path)
file_path