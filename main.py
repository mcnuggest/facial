import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np

face1 = image.imread("face1.jpg")

plt.imshow(face1)
plt.axis('off')
plt.show()