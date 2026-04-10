 🕵️‍♂️ Deepfake Sentinel: Hybrid Xception-LSTM Video Forensics 📹
📌 Project Overview

Deepfake Sentinel is an AI-powered video forensics system designed to detect manipulated (deepfake) videos using spatio-temporal analysis.

Unlike traditional image-based models that analyze frames independently, this system captures temporal inconsistencies—such as unnatural blinking, facial flickering, and lip-sync anomalies—across video sequences.

By combining Xception (CNN) for spatial feature extraction and Bidirectional LSTM (RNN) for temporal modeling, the system delivers a robust approach to digital media authentication.

🚀 Key Features
🧠 Hybrid Spatio-Temporal Model
TimeDistributed Xception for frame-level feature extraction
Bidirectional LSTM for sequence learning
🎯 Face Detection & Alignment
MTCNN ensures accurate face localization
Focuses model attention on facial artifacts only
⚡ Dynamic Data Pipeline
Real-time video decoding
Frame extraction, face cropping, normalization
📊 Forensic Output
Binary classification: Real / Fake
Confidence score for each prediction
🛠️ Technical Stack
Framework: TensorFlow / Keras
Computer Vision: OpenCV, MTCNN
Architecture: Xception + Bi-LSTM
Data Tools: NumPy, Pandas
Visualization: Matplotlib, Seaborn
Hardware: NVIDIA Quadro GV100 (CUDA acceleration)
📊 Dataset & Training
Dataset: Celeb-DF (Deepfake Dataset)
Sequence Length: 10 frames per sample
Frame Size: 224 × 224 RGB

Training Strategy:

Start-point randomization (skip first 30% of video)
Focus on dynamic facial motion rather than static frames
📈 Performance Results
Test Accuracy: 90%
Metric	Score
Precision (Fake)	91%
Recall (Fake)	91%
F1-Score	0.91
Overall Accuracy	90%

✅ Key Insight:
High recall (91%) ensures the model effectively detects manipulated videos, reducing the risk of false negatives in security applications.

📂 Project Structure
├── DEEP_FAKE.ipynb            # Model architecture & training  
├── Final_Deepfake_Model.keras # Trained model weights  
├── MTCNN_Logic/               # Face detection scripts  
├── README.md                  # Documentation  
└── requirements.txt           # Dependencies  
💻 How to Run
# Clone the repository
git clone https://github.com/your-username/Deepfake-Sentinel.git

# Install dependencies
pip install tensorflow mtcnn opencv-python matplotlib scikit-learn

Run the notebook and use:

check_specific_video("path_to_video.mp4")

to analyze any video file.

🛡️ Future Roadmap
 Add Spatio-Temporal Attention Maps for explainability
 Deploy via React-based dashboard (CyberShield SOC integration)
 Optimize for real-time inference using TensorRT
 Extend to multi-face tracking in complex scenes
⚠️ Disclaimer
