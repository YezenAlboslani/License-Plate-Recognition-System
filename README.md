# License Plate Recognition System (LPR)

This project demonstrates a **vehicle license plate recognition system** using Python, image processing, and machine learning.  
The system takes an image of a vehicle as input and outputs the characters on its license plate.

---

## 📖 Overview

The project is divided into three main stages:

1. **License Plate Detection**  
   - Locate the license plate region in the vehicle image.  
   - Techniques: grayscale conversion, binary thresholding, connected component analysis (CCA), and filtering by geometric properties.

2. **Character Segmentation**  
   - Extract and isolate individual characters from the detected license plate.  
   - Resize characters to a fixed dimension (20x20 pixels) for consistency.

3. **Character Recognition**  
   - Train a supervised machine learning model to classify segmented characters.  
   - Uses **Support Vector Classifier (SVC)** from `scikit-learn` for recognition.

---

## 🛠️ Requirements

- Python 3.x
- [scikit-image](https://scikit-image.org/)
- [numpy](https://numpy.org/)
- [scipy](https://scipy.org/)
- [matplotlib](https://matplotlib.org/)
- [Pillow](https://python-pillow.org/)
- [scikit-learn](https://scikit-learn.org/)

Install dependencies:

```bash
pip install -r requirements.txt