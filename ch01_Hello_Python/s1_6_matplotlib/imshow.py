import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("../../dataset/fox.jpg")

plt.imshow(img)
plt.title("Fox", fontsize = 20, fontweight = 'bold', color = '#022055')
plt.show()