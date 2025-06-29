
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Crea imagen simulando un aro "C" centrado (representado como círculo)
img = np.zeros((100, 100), dtype=np.uint8)
cv2.circle(img, (50, 50), 20, 255, 2)  # Aro C

blur = cv2.medianBlur(img, 5)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=100, param2=20, minRadius=15, maxRadius=25)

output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
if circles is not None:
    for c in circles[0, :]:
        center = (int(c[0]), int(c[1]))
        radius = int(c[2])
        cv2.circle(output, center, radius, (0, 255, 0), 2)
        cv2.circle(output, center, 2, (0, 0, 255), 3)
        print(f"Centro detectado del aro C: X={center[0]}, Y={center[1]}")

plt.imshow(output)
plt.title('Aro C detectado y centrado')
plt.axis('off')
plt.show()
