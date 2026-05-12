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
Dataset: [Celeb-DF-v2 (Kaggle)](https://www.kaggle.com/datasets/reubensuju/celeb-df-v2)
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

## 📂 Project Structure
├── DEEP_FAKE.ipynb            # Model architecture & training  
├── inference.py               # Standalone script for testing videos
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
└── README.md                  # Documentation  

*(Note: The trained model `Final_Deepfake_Model_CelebDF.keras` is generated after running the notebook and is required for `inference.py` to work.)*
## 💻 How to Run
# 1. Clone the repository
git clone https://github.com/your-username/Deepfake-Sentinel.git
cd Deepfake-Sentinel

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model (Optional if you already have the weights)
Run all cells in `DEEP_FAKE.ipynb` to train the model on the Celeb-DF dataset. 
This will generate `Final_Deepfake_Model_CelebDF.keras`.

# 4. Test a video using the inference script
python inference.py --video "path_to_video.mp4"

# OR test within the notebook using:
# check_specific_video("path_to_video.mp4")
## 🛡️ Future Roadmap
 Add Spatio-Temporal Attention Maps for explainability
 Deploy via React-based dashboard (CyberShield SOC integration)
 Optimize for real-time inference using TensorRT
 Extend to multi-face tracking in complex scenes
## ⚠️ Disclaimer
This project was built for educational and research purposes only. The creator does not condone the malicious use of deepfake technology. This tool is designed to *detect* digital forgery and assist in media authentication.
