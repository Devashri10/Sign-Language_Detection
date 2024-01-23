import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import os

# Load your model
classifier = load_model('ASLModel.h5')

# Other functions (e.g., fileSearch, load_images_from_folder, predictor, etc.) go here

def gesture_viewer():
    img = load_images_from_folder('TempGest/')
    index = 0

    def toggle_images_fwd():
        nonlocal index
        index += 1
        try:
            if 0 <= index < len(img):
                plt.axes()
                plt.imshow(img[index])
                plt.draw()
        except:
            pass

    def toggle_images_rev():
        nonlocal index
        index -= 1
        try:
            if 0 <= index < len(img):
                plt.axes()
                plt.imshow(img[index])
                plt.draw()
        except:
            pass

    fig, ax = plt.subplots()
    axcut = plt.axes([0.9, 0.0, 0.1, 0.075])
    axcut1 = plt.axes([0.0, 0.0, 0.1, 0.075])
    bcut = Button(axcut, 'Next', color='dodgerblue', hovercolor='lightgreen')
    bcut1 = Button(axcut1, 'Previous', color='dodgerblue', hovercolor='lightgreen')

    bcut.on_clicked(toggle_images_fwd)
    bcut1.on_clicked(toggle_images_rev)
    plt.show()

def main():
    st.title("Sign Language Recognition Dashboard")

    # Streamlit UI components go here

    if st.button("Create Gesture"):
        # Call the function for creating gestures
        create_gesture()

    if st.button("Export File"):
        # Call the function for exporting file
        export_file()

    if st.button("Gesture Viewer"):
        # Call the function for gesture viewer
        gesture_viewer()

    if st.button("Scan Sentence"):
        # Call the function for scanning sentence
        scan_sentence()

    if st.button("Scan Single Gesture"):
        # Call the function for scanning a single gesture
        scan_single_gesture()

if __name__ == "__main__":
    main()
