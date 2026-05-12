import os
import argparse
import numpy as np
import cv2
import tensorflow as tf
from mtcnn import MTCNN

def load_deepfake_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}. Please train the model first or provide the correct path.")
    print(f"Loading model from {model_path}...")
    return tf.keras.models.load_model(model_path)

def analyze_video(video_path, model):
    if not os.path.exists(video_path):
        print(f"❌ Error: Video file not found at {video_path}")
        return

    detector = MTCNN()
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    print(f"\n🔍 Processing: {os.path.basename(video_path)}...")
    print("Please wait, extracting faces for analysis...")

    while len(frames) < 10:
        ret, frame = cap.read()
        if not ret: 
            break
        
        # Detect faces
        results = detector.detect_faces(frame)
        if results:
            x, y, w, h = results[0]['box']
            # Boundary safety check
            x, y = max(0, x), max(0, y)
            face = frame[y:y+h, x:x+w]
            
            if face.size != 0:
                face = cv2.resize(face, (224, 224)) / 255.0
                frames.append(face)
        
        # Move forward 3 frames to speed up processing and get temporal variance
        for _ in range(3): 
            cap.grab()

    cap.release()

    if len(frames) == 10:
        # Convert to model format: batch_size of 1, sequence length of 10
        input_data = np.expand_dims(frames, axis=0)
        prediction = model.predict(input_data, verbose=0)[0][0]
        
        # > 0.5 is Fake, <= 0.5 is Real based on training logic
        label = "FAKE" if prediction > 0.5 else "REAL"
        confidence = prediction if prediction > 0.5 else (1 - prediction)
        
        print("\n" + "="*40)
        print(f"   DETECTION RESULT: {label}")
        print(f"   CONFIDENCE: {confidence*100:.2f}%")
        print("="*40 + "\n")
    else:
        print("❌ Model could not find 10 clear face frames in this video.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deepfake Sentinel Video Analysis")
    parser.add_argument("--video", type=str, required=True, help="Path to the video file to analyze")
    parser.add_argument("--model", type=str, default="Final_Deepfake_Model_CelebDF.keras", help="Path to the trained keras model")
    
    args = parser.parse_args()
    
    try:
        model = load_deepfake_model(args.model)
        analyze_video(args.video, model)
    except Exception as e:
        print(f"Error: {e}")
