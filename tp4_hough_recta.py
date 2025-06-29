
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Crea una imagen con una línea que simula el eje H
img = np.zeros((100, 100), dtype=np.uint8)
cv2.line(img, (10, 50), (90, 50), 255, 2)  # Eje H (horizontal)

edges = cv2.Canny(img, 50, 150)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)

output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a * rho, b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(output, pt1, pt2, (0, 0, 255), 1)

plt.imshow(output)
plt.title('Eje H detectado')
plt.axis('off')
plt.show()
