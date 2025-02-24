import cv2 as cv
import dlib
import time
import numpy as np
import threading
from playsound import playsound  # Install with: pip install playsound  

# Load Dlib's Face Detector and Landmark Predictor
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(r'facial-landmarks-recognition\shape_predictor_68_face_landmarks.dat')

# Indices for the eye landmarks in Dlib's 68-point model
LEFT_EYE_LANDMARKS = [36, 37, 38, 39, 40, 41]
RIGHT_EYE_LANDMARKS = [42, 43, 44, 45, 46, 47]

# Start Video Capture
cap = cv.VideoCapture(0)

closed_time = None  # Track time for eye closure
alarm_playing = False  # Flag to prevent multiple alerts

def play_alert():
    """Play alert sound in a separate thread to avoid freezing."""
    global alarm_playing
    playsound(r"data\alert.mp3")  # Ensure alert.mp3 exists
    alarm_playing = False

def calculate_EAR(eye_points):
    """Calculate Eye Aspect Ratio (EAR) to detect drowsiness."""
    A = np.linalg.norm(np.array(eye_points[1]) - np.array(eye_points[5]))  # Vertical distance
    B = np.linalg.norm(np.array(eye_points[2]) - np.array(eye_points[4]))  # Vertical distance
    C = np.linalg.norm(np.array(eye_points[0]) - np.array(eye_points[3]))  # Horizontal distance

    ear = (A + B) / (2.0 * C)  # EAR formula
    return ear

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector(gray)

    eyes_detected = False  # Track if eyes are detected

    for face in faces:
        landmarks = landmark_predictor(gray, face)

        # Get left and right eye landmarks
        left_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in LEFT_EYE_LANDMARKS]
        right_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in RIGHT_EYE_LANDMARKS]

        # Compute EAR for both eyes
        left_EAR = calculate_EAR(left_eye)
        right_EAR = calculate_EAR(right_eye)
        avg_EAR = (left_EAR + right_EAR) / 2.0  # Average EAR

        if avg_EAR > 0.204:  # Eyes are OPEN
            eyes_detected = True  
            closed_time = None  # Reset timer
            print(avg_EAR)

        else:  # Eyes are CLOSED
            if closed_time is None:  
                closed_time = time.time()  # Start timer when eyes first close

            # Check if eyes have been closed for more than 2 seconds
            if closed_time and (time.time() - closed_time > 2) and not alarm_playing:
                print("🚨 DROWSINESS ALERT! Eyes closed for too long. 🚨")
                alarm_playing = True  
                threading.Thread(target=play_alert, daemon=True).start()  # Play sound in background

        # Draw eye landmarks
        for (ex, ey) in left_eye + right_eye:
            cv.circle(frame, (ex, ey), 2, (255, 255, 255), -1)

    if not eyes_detected:
        print("❌ No eyes detected!")

    cv.imshow("Drowsiness Detection", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
