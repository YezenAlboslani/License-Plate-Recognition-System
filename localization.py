from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

car_image = imread("car.jpg", as_gray=True)
# it should be a 2 dimenstional array
print(car_image.shape)

# this next line is not needed, but since grey scale pixel
# in skimage ranges from 0 to 1, multiplying by 255 makes it
# range from 0 to 255, making it easier to deal with
gray_car_image = car_image * 255
fig, (ax1, ax2) = plt.subplots(1,2)
ax1.imshow(gray_car_image, cmap="gray")
threshold_value = threshold_otsu(gray_car_image)
binary_car_image = gray_car_image > threshold_value
ax2.imshow(binary_car_image, cmap="gray")
plt.show()