# Real-Time Object Detection for Robotic Sorting

> **Status:** Work in Progress

## Overview
This project aims to build an end-to-end computer vision pipeline for simulated robotic sorting tasks. The system utilizes a Convolutional Neural Network (CNN) to identify and localize industrial components (such as nuts and bolts) in real-time via a webcam feed.

## Tech Stack
* **Language:** Python 3.10
* **Deep Learning:** PyTorch, Torchvision
* **Computer Vision:** OpenCV (cv2)
* **Data Processing:** NumPy

## Current Progress
- [x] **Environment Setup:** Configured Conda environment with PyTorch and OpenCV.
- [x] **Camera Integration:** Implemented real-time webcam video capture and display loop (`main.py`).
- [x] **Data Sanity Check & Preprocessing:** Engineered a script (`check_data.py`) to parse YOLO-format `.txt` labels, translating normalized center-point ratios $(x, y, w, h)$ into absolute bounding box pixel coordinates for visual validation on the Kaggle Synthetic Nuts and Bolts dataset.

## Next Steps
- [ ] Build a custom PyTorch `Dataset` and `DataLoader` to feed images into the neural network.
- [ ] Design and implement the CNN architecture.
- [ ] Write the training loop, configure the loss function, and optimize model weights.
- [ ] Integrate the trained model with the live OpenCV webcam feed for real-time inference.
