# **Laboratorio #2: Multi Layer Perceptron**  
**Curso:** CC3092 Deep Learning y Sistemas Inteligentes  

**Integrantes:** 
- Mathew Cordero Aquino 22982
- Pedro Pablo Guzman 22111  
---

## **Objetivo**
El presente laboratorio tiene como objetivo comprender y modificar el comportamiento de una red neuronal de tipo Multi Layer Perceptron (MLP) implementada de manera manual y con la librería Pytorch. A través de estas modificaciones se busca entender el impacto de la función de pérdida y de la inicialización de parámetros en el proceso de aprendizaje.

---

## **Actividades**

### **1. Implementación de Binary Cross Entropy**
Se debe modificar la función `cost_function` para que, en lugar de calcular el error cuadrático medio (MSE), utilice la función de **binary cross entropy (BCE)**.  
Esto permitirá que la red se enfoque en la probabilidad de clasificación correcta en tareas binarias.

---

### **2. Ajuste de las variables delta en la retropropagación**
En la función `fit`, se deben actualizar las variables `delta1` y `delta2` para reflejar el nuevo cálculo de gradientes que deriva de la función BCE.  
Este ajuste es esencial para que la propagación hacia atrás funcione correctamente con la nueva función de pérdida.

---

### **3. Implementación de cambios en Pytorch**
Los mismos cambios realizados en la red implementada manualmente deben aplicarse en la versión de Pytorch, es decir:

- Aqui cambiamos a Binary Cross Entropy
![alt text](image.png)

- Autograd ya aplica la backpropagation, no es necesario hacer uso de otras cosas


---

### **4. Documentación del código**
Agregar comentarios explicativos en cada función, describiendo:
- Su propósito dentro del flujo de la red.
- El tipo de etapa en la que esta

![alt text](image-1.png)

Todo el codigo esta en el jupyter
---

### **5. Comparación de la función de pérdida**
Se debe graficar y comparar la evolución de la función de pérdida durante el aprendizaje en ambas redes (implementación manual vs. Pytorch) para evaluar posibles diferencias de convergencia y desempeño.

---

## **Preguntas de análisis**

1. **¿Existen cambios de arquitectura en las 2 redes implementadas?**  
   Explicar si las modificaciones en la función de pérdida impactan la arquitectura de las redes.

2. **¿Existen diferencias en la velocidad de convergencia entre las 2 redes?**  
   Analizar la gráfica de la función de pérdida y el número de iteraciones necesarias para converger.

3. **Inicialización de parámetros en `init_parameters`:**  
   - ¿Qué sucede si inicializamos los pesos en `0` en lugar de valores aleatorios?  
   - ¿Qué ocurre si hacemos lo mismo con los *bias*?  
   Justificar el impacto que esto tendría en la simetría de los gradientes y el aprendizaje de la red.

---
