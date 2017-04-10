import matplotlib.pyplot as plt

counts = [15, 16, 18, 20 ,22]
dynamic = [0.000281095504761, 0.000301122665405, 0.000349998474121, 0.000365018844604, 0.000380992889404]
recursive = [0.527917861938, 1.51841020584, 8.46917390823, 54.8444831371, 269.672949076]

plt.subplot(211)
plt.plot(counts, dynamic, "ro-", label="Dynamic Method", color="red")
plt.ylabel("Y axis (Time)")
plt.legend(loc="lower right")

plt.subplot(212)
plt.plot(counts, recursive, "ro-", label="Recursive Method", color="red")
plt.ylabel("Y axis (Time)")
plt.xlabel("X axis (M+N)")
plt.legend(loc="upper left")

plt.show()