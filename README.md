# Visualizacion-de-data-matematica
Este documento en en GitHub es para subir la aplicación de mi pensamiento probabilístico en python.

#Pre-requisitos 📋
Dado que trabajo en PYTHON, de momento solo basta con instalar las distintas librerías y llamarlas en las primeras lineas del programa.
Estas son sys, mathplotlib y panda.
```
import matplotlib
```
#Ejecución de prueba: Cálculo de PI ⚙️:
```
python3 calculo_pi.py   # Ejecutamos nuestro script.

# Y estos serán nuestros resultados.
Est=3.14234, sigma=0.02594, agujas=1000
Est=3.13966, sigma=0.01795, agujas=2000
Est=3.143, sigma=0.01272, agujas=4000
Est=3.14076, sigma=0.00949, agujas=8000
Est=3.14142, sigma=0.00678, agujas=16000
Est=3.14154, sigma=0.00457, agujas=32000
```

#Integración de mathplotlib y panda 📦:
```
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.DataFrame({'Días':['L', 'M', 'X', 'J', 'V', 'S', 'D'], 
                   'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 
                   'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]})
fig, ax = plt.subplots()
df.plot(x = 'Días', y = 'Madrid', ax = ax)
df.plot(x = 'Días', y = 'Barcelona', ax = ax)
plt.show()
```

