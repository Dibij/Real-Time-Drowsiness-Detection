# Drowsiness Detection System 🚀  

## **Overview**  
Drowsiness Detection System is a **computer vision-based project** that uses **Dlib** and **OpenCV** to monitor eye movements and detect drowsiness. If the system detects **prolonged eye closure**, it triggers an **alert sound** to warn the user.  

## **Features**  
- **Eye Detection:** Uses **Dlib’s 68 facial landmarks** to track eye movement.  
- **Drowsiness Alert:** If eyes remain closed for **2+ seconds**, an alarm is triggered.  
- **Real-Time Processing:** Works with a webcam to analyze eye closure in real time.  
- **Non-Blocking Sound Alert:** Uses threading to play an **alert sound** without freezing the program.  

## **Installation**  
### **Prerequisites**  
- Python 3.x  

### **Setup**  
#### 1. Clone the repository:  
   ```bash
   git clone https://github.com/Dibij/Drowsiness-Detection.git
   cd Drowsiness-Detection
   ```
#### 2. Install dependencies:
```bash
pip install -r requirements.txt
```
Ensure that the shape predictor model (shape_predictor_68_face_landmarks.dat) and alert sound (alert.mp3) are in the correct directory.
#### 3. Usage
Navigate to the src directory and run the detection system:

``` bash
cd src  
python main.py  
```
#### 4. Controls
Drowsiness Alert: The system automatically triggers a sound if drowsiness is detected.
Quit: Press Q to exit the program.
File Structure
``` bash
Drowsiness-Detection/
│── data/
│   ├── alert.mp3         # Sound alert for drowsiness
│   ├── shape_predictor_68_face_landmarks.dat  # Dlib model for facial landmarks
│── src/
│   ├── main.py           # Main script for real-time drowsiness detection
│── requirements.txt      # Required dependencies
│── README.md             # Documentation
```
#### 5. Notes
- The system is a work in progress, and I hope to improve it in the future.
- Potential future upgrades:
- Use a deep learning model for better accuracy.
- Implement head pose detection to improve drowsiness tracking.
#### 6. License
This project is open-source—feel free to modify and enhance it! 🚀


