# Detección de Formas con Transformada de Hough

Este proyecto implementa dos prototipos independientes que permiten detectar características geométricas (líneas y circunferencias) sobre imágenes binarizadas, aplicando la Transformada de Hough como herramienta central.

El objetivo es identificar automáticamente la posición del aro "C" y su relación con el eje horizontal "H" en una imagen simulada, como paso previo al montaje preciso de un motor en una línea de producción automatizada.

## Descripción

Se desarrollan dos programas:

- **Transformada de Hough para Rectas:** se detecta el eje "H" que atraviesa el centro de la imagen.
- **Transformada de Hough para Circunferencias:** se detecta la ubicación del aro "C" de radio conocido.

Ambos prototipos trabajan sobre imágenes sintéticas y fueron adaptados para representar el problema real del alineado del aro sobre el motor. El sistema permite detectar la posición central del aro (coordenadas X e Y), lo cual es fundamental para garantizar el correcto ensamble automatizado.

---

## Contenido del Repositorio

| Archivo                             | Descripción                                                             |
|-------------------------------------|-------------------------------------------------------------------------|
| `tp4_hough_lineas.py`               | Script que implementa la detección de líneas horizontales (eje H).      |
| `tp4_hough_circulos.py`             | Script que implementa la detección de circunferencias (aro C).          |
| `README.md`                         | Descripción general del proyecto.                                       |

---

## Cómo ejecutar

### Requisitos:
- Python 3.x
- Numpy
- OpenCV (cv2)
- Matplotlib

### Ejecución:

```bash
python tp4_hough_lineas.py
```
o

```bash
python tp4_hough_circulos.py
```

---

## Ejemplo

El programa generará una imagen binaria con un aro y un eje horizontal (simulando una imagen del motor), luego mostrará visualmente:

- **En el caso de líneas:** la recta detectada superpuesta sobre la imagen.
- **En el caso de círculos:** la circunferencia detectada y el centro estimado marcado.

---

## Autor

Iván Bustamante  
Trabajo práctico para la materia de Inteligencia Artificial - Módulo 4  
2025
