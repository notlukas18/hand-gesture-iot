import cv2
import mediapipe as mp
import time
import paho.mqtt.client as mqtt

MQTT_BROKER = "34.27.113.8"
MQTT_PORT = 1883
MQTT_USER = "pablo"
MQTT_PASS = "idunno"

client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

prev_finger_status = {"thumb": None, "index": None, "middle": None, "ring": None, "pinky": None}
last_request_time = {k: 0 for k in prev_finger_status}
REQUEST_INTERVAL = 0.2

def can_send(finger):
    now = time.time()
    if now - last_request_time[finger] >= REQUEST_INTERVAL:
        last_request_time[finger] = now
        return True
    return False

def control_led(finger, state):
    if not can_send(finger): return
    topic = f"hand/led/{finger}"
    client.publish(topic, state)
    print(f"Sent {state.upper()} to {finger}")

def check_fingers_state(hand_landmarks, hand_label):
    thumb_up = (hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x <
                hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x) if hand_label == "Right" else (
                hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x >
                hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x)

    index_up = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_up = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_up = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_up = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y

    return {
        "thumb": thumb_up,
        "index": index_up,
        "middle": middle_up,
        "ring": ring_up,
        "pinky": pinky_up
    }

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera not found")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks and results.multi_handedness:
            for landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                label = handedness.classification[0].label
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                fingers = check_fingers_state(landmarks, label)
                for finger, is_up in fingers.items():
                    if prev_finger_status[finger] != is_up:
                        control_led(finger, "on" if is_up else "off")
                        prev_finger_status[finger] = is_up

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    client.loop_stop()

if __name__ == "__main__":
    main()
