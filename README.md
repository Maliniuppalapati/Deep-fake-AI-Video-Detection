# Deep Fake AI Video Detection

A deep learning-based project to detect whether a video is **real** or **deepfake** using AI and computer vision techniques.  
This project processes video frames, extracts useful features, and applies a trained model to classify videos as **fake** or **real**.

## Overview

Deepfakes are AI-generated or AI-manipulated videos that can make a person appear to say or do something they never actually did.  
The goal of this project is to build a system that can analyze video content and identify manipulated media.

This notebook-based project focuses on:

- Video preprocessing
- Frame extraction
- Face/frame analysis
- Model training/testing
- Deepfake classification

## Features

- Detects whether a video is **real** or **fake**
- Uses **AI / Deep Learning** for classification
- Extracts frames from videos for analysis
- Can be extended for real-world deepfake detection systems
- Implemented in **Python** using **Jupyter Notebook**

## Tech Stack

- Python
- Jupyter Notebook
- OpenCV
- NumPy
- Pandas
- Matplotlib
- TensorFlow / Keras *(if used)*
- Scikit-learn *(if used)*

## Project Structure

```bash
Deep-fake-AI-Video-Detection/
│── DEEP_FAKE.ipynb
│── README.md

How It Works

Input Video

The system takes a video as input.

Frame Extraction

The video is split into multiple frames.

Preprocessing

Frames are resized, normalized, and prepared for analysis.

Feature Extraction / Model Processing

Important patterns are extracted from frames.

Prediction

The trained model predicts whether the video is real or deepfake.

Installation

Clone the repository:

git clone https://github.com/Maliniuppalapati/Deep-fake-AI-Video-Detection.git
cd Deep-fake-AI-Video-Detection

Install required libraries:
pip install opencv-python numpy pandas matplotlib scikit-learn tensorflow

Usage

Open the notebook:
jupyter notebook DEEP_FAKE.ipynb

Run the cells step by step to:

load the dataset

preprocess videos/frames

train the model

evaluate results

test predictions

Dataset

This project requires a dataset containing real and fake videos.

You can use datasets such as:

FaceForensics++

DeepFake Detection Challenge (DFDC)

Celeb-DF

Make sure the dataset is placed in the correct folder path before running the notebook.

Output

The model predicts:

Real Video

Fake Video

It may also show:

accuracy

loss

confusion matrix

training/validation graphs

Applications

Fake media detection

Social media content verification

Cybersecurity and digital forensics

Journalism and fact-checking

Misinformation prevention

Future Improvements

Improve model accuracy

Add support for real-time video detection

Build a web app for user uploads

Use advanced CNN/LSTM architectures

Detect manipulated facial regions more precisely

Results

The notebook demonstrates the training and testing process for deepfake video detection.
Results depend on the dataset, preprocessing quality, and model architecture used.
