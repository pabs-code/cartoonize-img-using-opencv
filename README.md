# Cartoonizing an Image Using Opencv

A Streamlit-based application that allows users to upload an image and apply one of three cartoonization techniques to transform it into a stylized cartoon version.

## Table of Contents

  - [About the Project](#-about-the-project)
    - [What Cartoonizer Techniques are Used?](#what-cartoonizer-techniques-are-used)
    - [How It Works:](#how-it-works)
  - [Features](#-features)
  - [Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
  - [Installation](#-installation)
  - [Running Script](#-running-script)
  - [Expectations When Running This App](#-expectations-when-running-this-app)
  - [Demo](#-demo)
  - [Acknowledgments](#-acknowledgments)
  - [License](#-license)

---

## About the Project

### What Cartoonizer Techniques are Used?

This **Cartoonizer App** is a simple yet powerful image processing tool that applies different cartoonization techniques to an uploaded image. It uses **OpenCV** and **Streamlit** for performance, visualization, and user interaction.

### How It Works:

The app applies one of the following techniques to generate a cartoon-style version of the input image:

1. **Bilateral Filtering + Edge Detection** – Smooths and sharpens edges for a cartoon-like effect.
2. **Color Quantization + Edge Enhancement** – Reduces colors and sharpens edges for a more stylized look.
3. **Laplacian Edge Detection** – Uses edge detection to enhance sharpness and detail.

The user can select a technique, upload an image, and view both the original and cartoonized versions on the app.

---

## Features

- Easy-to-use **Streamlit** interface.
- Supports common image formats: `.jpg`, `.jpeg`, and `.png`.
- Three different cartoonization techniques:
  - Bilateral Filtering + Edge Detection
  - Color Quantization + Edge Enhancement
  - Laplacian Edge Detection
- Real-time preview of the original and cartoonized image.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

| Dependency | Version |
| ---------- | ------- |
| Python     | 3.8+    |
| Streamlit  | ≥1.20   |
| OpenCV     | ≥4.5    |
| Pillow     | ≥9.1    |

You can install them using pip:

```bash
pip install streamlit opencv-python pillow
```

---

## Installation

To install and run the app locally:

```bash
# Clone this repository (if needed)
git clone https://github.com/YOUR_GITHUB_USERNAME/img-cartoonizer-using-opencv.git
cd img-cartoonizer-using-opencv

# Install dependencies
pip install streamlit opencv-python pillow

# Run the app
streamlit run app.py
```

---

## Running Script

Once installed, simply run the following command in your terminal:

```bash
streamlit run app.py
```

This will launch the Streamlit application in your browser, where you can interact with the app.

---

## Expectations When Running This App

- The user must upload an image in `.jpg`, `.jpeg`, or `.png` format.
- One of the three cartoonization techniques must be selected from the dropdown menu.
- The output will display both the original and cartoonized versions of the image side-by-side.

> ⚠️ If no file is uploaded or a method is not selected, the app will not show any processed image.

---

## Demo

Here’s a quick overview of how the app looks in action:

1. Open your browser and go to `http://localhost:8501` (or the URL provided by Streamlit).
2. Upload an image.
3. Select a cartoonization method.
4. View the original and processed images on the web app UI.

https://github.com/user-attachments/assets/eed42b99-be5f-470f-ba0c-0733e301a8e0

---

## Acknowledgments

- **Streamlit** – For the easy-to-use UI.
- **OpenCV** – For powerful image processing capabilities.
- **Pillow (PIL)** – For handling and displaying images in the app.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---
