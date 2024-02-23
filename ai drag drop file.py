import cv2
import mediapipe as mp
import pyautogui
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
# Set up the initial position of the mouse
pyautogui.moveTo(x=100, y=100)
# Start the webcam
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        # Flip the image horizontally for a mirror effect
        image = cv2.flip(image, 1)
        # Convert the image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Process the image with Mediapipe
        results = hands.process(image)
        # Check if hands are detected in the image
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get the coordinates of the index finger and thumb
                index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

                # Calculate the distance between the index finger and thumb
                # distance = ((thumb.x - index_finger.x) * 2 + (thumb.y - index_finger.y) * 2) ** 0.5
                distance = abs(complex(thumb.x, thumb.y) - complex(index_finger.x, index_finger.y))

                # If the distance is less than a threshold, simulate drag and drop
                if distance < 0.5:
                    # Simulate left click and hold
                    pyautogui.mouseDown()

                    # Move the mouse to drag the file
                    pyautogui.moveTo(x=thumb.x * image.shape[1], y=thumb.y * image.shape[0], duration=0.5)

                    # Release the left click to drop the file
                    pyautogui.mouseUp()

        # Convert the image back to BGR format
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Display the image
        cv2.imshow('Virtual Mouse', image)
        cv2.waitKey(5)
        time.sleep(0.05)


