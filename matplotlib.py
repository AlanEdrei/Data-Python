import matplotlib.pyplot as plt

eje_x = ["a","b","c","d","e"]
datos1 = [10, 20, 30, 40, 50]
datos2 = [20, 30, 40, 50, 60]


plt.plot(eje_x, datos1)
plt.show()

plt.plot(eje_x, datos2)
plt.show()

#Example: 5-level Student Certification Exam

import numpy as np

años = ["2011", "2012", "2013", "2014", "2015",
        "2016", "2017", "2018", "2019", "2020"]

nivel1 = np.random.rand(10)*100
nivel2 = np.random.rand(10)*200 + 100
nivel3 = np.random.rand(10)*300 + 200
nivel4 = np.random.rand(10)*400 + 300
nivel5 = np.random.rand(10)*500 + 400

# Chart Customization

# Enter data series with color, marker, label and style

plt.plot(años, nivel1, label="Nivel 1", color="purple", marker="<", linestyle="-")
plt.plot(años, nivel2, label="Nivel 2", color="red", marker="*", linestyle="--")
plt.plot(años, nivel3, label="Nivel 3", color="blue", marker="^", linestyle=":")
plt.plot(años, nivel4, label="Nivel 4", color="black", marker=".", linestyle="-.")
plt.plot(años, nivel5, label="Nivel 5", color="green", marker="+", linestyle=" ")

# Activate legends
plt.legend()

# Títle
plt.title("Examen de Certificación")

# Labels
plt.xlabel("Años que se ha realizado el examen")
plt.ylabel("Puntaje")

# Customize Score Axis from 0 to 1000 in increments of 50

plt.yticks(np.arange(0, 1001, 50))

# grid

plt.grid()

# Activate minor marks
plt.minorticks_on()

plt.show()
