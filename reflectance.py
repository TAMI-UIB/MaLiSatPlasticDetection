import numpy as np
import rasterio
import matplotlib.pyplot as plt


with rasterio.open('Almeria65.tif') as src:
    image = src.read()
image = np.moveaxis(image, 0, -1)

with rasterio.open('mascara65.tif') as mask_src:
    mask = mask_src.read(1)

with rasterio.open('mascara_water65.tif') as mask_src:
    mask_terra = mask_src.read(1)

plastic_pixels = image[mask == 100]
pixels_terra = image[mask_terra == 100]

plastic_signature = np.mean(plastic_pixels, axis=0)
std_signature = np.std(plastic_pixels, axis=0)

terra = np.mean(pixels_terra, axis=0)
std_terra = np.std(pixels_terra, axis=0)

wavelengths = np.loadtxt('wavelenghts65.txt')
mask_non_zero = (wavelengths != 1606.4913) &  (wavelengths != 1616.8336)
wavelengths_filtered = wavelengths[mask_non_zero]
plastic_signature_filtered = plastic_signature[mask_non_zero]
water_filtered = terra[mask_non_zero]



plt.plot(wavelengths_filtered, plastic_signature_filtered, label="Plastic", color='black')
plt.plot(wavelengths_filtered, water_filtered, label="Water", color='blue')

plt.xlabel("Wavelength")
plt.ylabel("Reflectance")
plt.title("Espectre")
plt.legend()
plt.grid(True)
plt.savefig("exemple.png", dpi=300, bbox_inches='tight')
