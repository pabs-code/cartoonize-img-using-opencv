# cartoonize-img-using-opencv


This repository provides a practical guide to cartoonizing images using three different techniques in Python with OpenCV and NumPy. Each method applies a unique combination of image processing steps to transform a photo into a stylized cartoon.

- Method 1: Applying Bilateral Filtering and Edge Detection
    - Uses bilateral filtering to preserve edges while smoothing the image.
    - Combines it with edge detection (e.g., Canny) to create a sharp, cartoon-like outline.

- Method 2: Color Quantization and Edge Enhancement
    - Reduces the number of colors in the image using color quantization to create a limited palette.
    - Enhances edges with sharpening techniques to add contrast and stylization.

- Method 3: Enhancing Edges with a Combination of Filters
    - Combines multiple filters such as Gaussian blur, Sobel edge detection, and adaptive thresholding to create a more detailed cartoon effect.
