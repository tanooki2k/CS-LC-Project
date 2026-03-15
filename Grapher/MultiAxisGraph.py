import matplotlib.pyplot as plt
import numpy as np

hours = np.arange(24)

temperature = 20 + 8*np.sin(np.linspace(0, 2*np.pi, 24))
risk = 50 + 30*np.sin(np.linspace(0, 2*np.pi, 24) + 0.8)

moisture = np.array([
False, False, True, True, False, False,
True, False, False, True, True, False,
False, False, True, False, False, False,
True, True, False, False, False, True
])


fig, ax1 = plt.subplots()

temp_line, = ax1.plot(hours, temperature, label="Temperature (°C)", color="orange")
ax1.set_xlabel("Hour")
ax1.set_ylabel("Temperature (°C)")

ax2 = ax1.twinx()
risk_line, = ax2.plot(hours, risk, label="Risk (0% - 100%)", color="blue")
ax2.set_ylabel("Risk (0% - 100%)")

false_idx = moisture == False
true_idx = moisture == True

moist_false = ax1.scatter(
    hours[false_idx],
    temperature[false_idx],
    color="red",
    marker="x",
    label="Moisture = False"
)

moist_true = ax1.scatter(
    hours[true_idx],
    temperature[true_idx],
    color="green",
    marker="o",
    label="Moisture = True"
)


lines = [temp_line, risk_line, moist_false, moist_true]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper right")

plt.show()