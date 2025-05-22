import numpy as np
import matplotlib.pyplot as plt

L = 1000
k = 0.5
y0 = 100
A = (L / y0) - 1  # 9

t = np.linspace(0, 20, 400)
y = L / (1 + A * np.exp(-k * t))

plt.figure(figsize=(8, 5))
plt.plot(t, y, linewidth=2, label=r'$y(t)=\frac{1000}{1+9e^{-0.5t}}$')
plt.axhline(L, linestyle='--', color='gray', linewidth=1)
plt.text(0.5, 1030, 'Carrying capacity (1000)', va='bottom')
plt.title("Mr. Moy's Croissant Production (Logistic Growth)")
plt.xlabel('Time (t)')
plt.ylabel('Croissants (y)')
plt.grid(True)
plt.legend()
plt.tight_layout()

file_path = "logistic_crossaint_curve.png"
plt.savefig(file_path)
file_path
