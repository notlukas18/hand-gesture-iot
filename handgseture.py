import cv2
import mediapipe as mp
import requests
import time

ESP32_IP = "http://192.168.62.34"  # Your ESP32 IP address

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

prev_all_status = None  # Track all LEDs on/off state
prev_finger_status = {
    "thumb": None,
    "index": None,
    "middle": None,
    "ring": None,
    "pinky": None
}

# Track last request time per finger to avoid spamming
last_request_time = {
    "all": 0,
    "thumb": 0,
    "index": 0,
    "middle": 0,
    "ring": 0,
    "pinky": 0
}

REQUEST_INTERVAL = 0.15  # 150 ms delay between requests per finger/all

# Map fingers to LED colors or IDs if needed
finger_led_colors = {
    "thumb": "yellow",
    "index": "red",
    "middle": "green",
    "ring": "blue",
    "pinky": "white"
}

def can_send(finger):
    now = time.time()
    if now - last_request_time[finger] >= REQUEST_INTERVAL:
        last_request_time[finger] = now
        return True
    return False

def control_led(finger, state):
    if not can_send(finger):
        return

    url = f"{ESP32_IP}/led/{finger}/{state}"
    try:
        response = requests.get(url, timeout=1)
        print(f"{finger.capitalize()} {state.upper()}: {response.text}")
    except Exception as e:
        print(f"Failed: {finger} {state} -> {e}")

def control_all_leds(state):
    if not can_send("all"):
        return

    for finger in finger_led_colors.keys():
        control_led(finger, state)

def check_fingers_state(hand_landmarks, hand_label):
    if hand_label == "Right":
        thumb_up = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
    else:
        thumb_up = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x

    index_up = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_up = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_up = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_up = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y

    fingers = {
        "thumb": thumb_up,
        "index": index_up,
        "middle": middle_up,
        "ring": ring_up,
        "pinky": pinky_up
    }

    return fingers

def main():
    global prev_all_status, prev_finger_status

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                hand_label = hand_handedness.classification[0].label  # "Left" or "Right"
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                fingers = check_fingers_state(hand_landmarks, hand_label)
                all_up = all(fingers.values())
                all_down = not any(fingers.values())

                # Only trigger all LEDs on/off if state changed from previous
                if all_up and prev_all_status != "on":
                    control_all_leds("on")
                    prev_all_status = "on"
                    # Update individual finger states
                    for f in fingers.keys():
                        prev_finger_status[f] = True

                elif all_down and prev_all_status != "off":
                    control_all_leds("off")
                    prev_all_status = "off"
                    for f in fingers.keys():
                        prev_finger_status[f] = False

                else:
                    # Partial fingers state: reset all-status
                    prev_all_status = None
                    # Control each finger individually if changed
                    for finger, is_up in fingers.items():
                        if prev_finger_status[finger] != is_up:
                            state = "on" if is_up else "off"
                            control_led(finger, state)
                            prev_finger_status[finger] = is_up

        cv2.imshow("Hand Gesture Control", frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
