import streamlit as st
import cv2
import numpy as np
from PIL import Image


class CartoonizerApp:
    """
    Streamlit application to apply cartoonization techniques on uploaded images.

    Attributes
    ----------
    image : PIL.Image.Image or None
        The uploaded image.
    """

    def __init__(self):
        self.image = None

    def _setup_intro(self):
        """Set up the main introduction to explain what this app does."""
        st.markdown(
            """
            # 🎨 Cartoonizer - Choose Your Style!

            Welcome to the **Cartoonizer App**! This application allows you to upload an image and apply one of three cartoonization techniques to transform it into a stylized cartoon version.

            ### What You Can Expect
            - Upload an image in `.jpg`, `.jpeg`, or `.png` format.
            - Select one of the following cartoonization methods:
              1. **Bilateral Filtering + Edge Detection** – Smooths and sharpens edges for a cartoon-like effect.
              2. **Color Quantization + Edge Enhancement** – Reduces colors and sharpens edges for a more stylized look.
              3. **Laplacian Edge Detection** – Uses edge detection to enhance sharpness and detail.
            - View both the original and cartoonized versions of your image here below.

            Try it out with any photo you'd like to transform into a cartoon!
            """
        )

    def _setup_sidebar(self):
        """Set up the sidebar with instructions and branding."""
        st.sidebar.write(
            "Upload an image and choose a cartoonization technique.")

    def convert_to_numpy_and_bgr(self, image: Image) -> np.ndarray:
        """
        Convert PIL image to NumPy array and BGR format.

        Parameters
        ----------
        image : PIL.Image.Image
            Input RGB image to be processed.

        Returns
        -------
        numpy.ndarray
            Converted NumPy array in BGR format.
        """
        return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    def convert_to_pil(self, img: np.ndarray) -> Image:
        """
        Convert NumPy array to PIL image.

        Parameters
        ----------
        img : numpy.ndarray
            Input NumPy array in BGR format.

        Returns
        -------
        PIL.Image.Image
            Converted PIL image.
        """
        return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    def _apply_cartoonization(self, method: str, image: np.ndarray) -> Image:
        """
        Apply different cartoonization techniques to an image.

        Parameters
        ----------
        method : str
            The selected cartoonization method.
        image : numpy.ndarray
            Input BGR image to be processed.

        Returns
        -------
        PIL.Image.Image
            Cartoonized version of the input image.
        """

        if method == "Method 1: Bilateral + Edge Detection":
            cartoon_img = cv2.bilateralFilter(
                image, d=9, sigmaColor=75, sigmaSpace=75)
            gray = cv2.cvtColor(cartoon_img, cv2.COLOR_BGR2GRAY)
            blurred = cv2.medianBlur(gray, 7)
            edges = cv2.adaptiveThreshold(
                blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
            colored_edges = cv2.bitwise_and(
                cartoon_img, cartoon_img, mask=edges)
            return self.convert_to_pil(colored_edges)

        elif method == "Method 2: Color Quantization + Edge Enhancement":
            data = np.float32(np.array(image).reshape((-1, 3)))
            criteria = (cv2.TERM_CRITERIA_EPS +
                        cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
            ret, label, center = cv2.kmeans(
                data, 9, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
            center = np.uint8(center)
            result = center[label.flatten()]
            result = result.reshape(np.array(image).shape)
            gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
            blurred = cv2.medianBlur(gray, 7)
            edges = cv2.adaptiveThreshold(
                blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
            cartoon_img = cv2.bitwise_and(result, result, mask=edges)
            return self.convert_to_pil(cartoon_img)

        elif method == "Method 3: Laplacian Edge Detection":
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.medianBlur(gray, 5)
            edges = cv2.Laplacian(blurred, cv2.CV_8U, ksize=5)
            inverted_edges = 255 - edges
            cartoon_img = cv2.bitwise_or(image, image, mask=inverted_edges)
            return self.convert_to_pil(cartoon_img)

        else:
            raise ValueError("Invalid method selected")

    def run(self):
        """Main method to run the Streamlit application."""

        try:
            self._setup_intro()
            self._setup_sidebar()

            if uploaded_file := st.sidebar.file_uploader(
                "Upload an Image", type=["jpg", "jpeg", "png"]
            ):
                with st.spinner('Processing...'):
                    self.image = Image.open(uploaded_file)
                    original_image_np = self.convert_to_numpy_and_bgr(
                        self.image)

        except Exception as e:
            st.error(f"An error occurred: {e}")

        if self.image:
            method = st.sidebar.selectbox(
                "Select Cartoonization Technique",
                [
                    "Method 1: Bilateral + Edge Detection",
                    "Method 2: Color Quantization + Edge Enhancement",
                    "Method 3: Laplacian Edge Detection"
                ]
            )

            try:
                processed_image_np = self._apply_cartoonization(
                    method, original_image_np)
                st.image(self.image, caption="Original",
                         use_container_width=True)
                st.image(processed_image_np, caption="Cartoonized",
                         use_container_width=True)

            except Exception as e:
                st.error(
                    f"An error occurred while applying the cartoonization technique: {e}")


if __name__ == "__main__":
    app = CartoonizerApp()
    app.run()
