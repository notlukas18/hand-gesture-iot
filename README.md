# ✋🤖 Hand Gesture Controlled IoT System (ESP32 + Python + OpenCV + MediaPipe)

This project demonstrates a smart, contactless interface where users can control multiple LEDs using hand gestures via a webcam and an ESP32 microcontroller. It combines computer vision (MediaPipe + OpenCV) with IoT (ESP32, HTTP communication) to build a modern, accessible, and touchless system.

---

## 📌 Features

- Real-time hand gesture recognition using MediaPipe
- Individual control of 5 LEDs (Thumb, Index, Middle, Ring, Pinky)
- Turn all LEDs ON/OFF with universal gestures
- HTTP communication between Python and ESP32
- Modular and expandable design for smart home systems

---

## 🖼️ Demo

![image_2025-05-27_00-38-25](https://github.com/user-attachments/assets/a1754ec2-0746-4499-9113-327430af8fe0)

<img src="images/screenshots/gesture_example2.png" width="500"/>

---

## 🧠 How It Works

1. A webcam captures the video stream.
2. MediaPipe identifies hand landmarks.
3. Python processes gestures and sends HTTP requests.
4. The ESP32 receives the request and activates LEDs accordingly.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **MediaPipe & OpenCV** for hand gesture detection
- **ESP32** microcontroller with Arduino
- **HTTP server on ESP32**
- **Wiring Diagram made with Fritzing**

---

## ⚙️ Setup Instructions

### 1. ESP32 (Arduino)
- Install ESP32 board in Arduino IDE.
- Upload `led_control.ino` to your ESP32.
- Connect LEDs to ESP32 GPIO pins as per the wiring diagram.
- Connect ESP32 to the same Wi-Fi as your PC.

### 2. Python Client
```bash
pip install opencv-python mediapipe requests
````

* Replace the IP address in `gesture_control.py` with your ESP32’s IP.
* Run the script:

```bash
python gesture_control.py
```

---

## 🧪 Supported Gestures

| Gesture          | Action            |
| ---------------- | ----------------- |
| All fingers up   | Turn ALL LEDs ON  |
| All fingers down | Turn ALL LEDs OFF |
| Thumb only up    | Yellow LED ON     |
| Index only up    | Red LED ON        |
| Middle only up   | Green LED ON      |
| Ring only up     | Blue LED ON       |
| Pinky only up    | White LED ON      |

---

## 🧩 Future Improvements

* Replace HTTP with MQTT for real-time efficiency
* Add voice command integration
* Support multi-hand recognition
* Create mobile app for remote control
* Integrate with platforms like Home Assistant

---

## 🔒 Ethical and Social Impact

* All video processing is done **locally**, preserving user privacy.
* The system can help users with mobility/speech impairments.
* Energy-efficient using low-power ESP32 boards.
* Inclusive design adaptable for different gestures or cultures.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to improve gesture recognition, UI, or support other hardware, feel free to fork the repo.

---

## 🙋‍♂️ Author

**Abduvahhobov Javohir**
Final Year Project – IoT Internship
Tashkent Turin Polytechnic University

```
