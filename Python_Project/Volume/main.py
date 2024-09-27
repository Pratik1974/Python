import cv2
import numpy as np
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Volume control setup using pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get volume range (-65.25 to 0.0)
volume_range = volume.GetVolumeRange()
min_vol = volume_range[0]
max_vol = volume_range[1]

# Video capture setup
cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while True:
        success, img = cap.read()
        if not success:
            break

        # Flip the image horizontally for a selfie-view display
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the image and find hands
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Drawing hand landmarks
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get landmarks of thumb and index finger
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Get coordinates
                thumb_x, thumb_y = int(thumb_tip.x * img.shape[1]), int(thumb_tip.y * img.shape[0])
                index_x, index_y = int(index_tip.x * img.shape[1]), int(index_tip.y * img.shape[0])

                # Draw circles on thumb and index finger tips
                cv2.circle(img, (thumb_x, thumb_y), 10, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (index_x, index_y), 10, (255, 0, 255), cv2.FILLED)

                # Draw a line between thumb and index finger
                cv2.line(img, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 255), 3)

                # Calculate distance between thumb and index finger
                length = np.hypot(index_x - thumb_x, index_y - thumb_y)

                # Volume control: map the length to volume range
                vol = np.interp(length, [30, 250], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

                # Display the volume bar
                vol_bar = np.interp(length, [30, 250], [400, 150])
                cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
                cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)

        # Display the image
        cv2.imshow("Volume Control", img)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
