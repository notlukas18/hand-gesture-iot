# ✋🤖 Hand Gesture Controlled IoT System  
**(ESP32 + Python + OpenCV + MediaPipe + MQTT)**

This final-year project demonstrates a smart, contactless interface where users can control multiple LEDs using hand gestures detected via a webcam. It combines **Computer Vision** (MediaPipe + OpenCV) with **IoT** (ESP32 + MQTT communication), offering a modern, accessible, and touchless solution for smart environments.

---

## 📌 Features

- 🖐️ Real-time hand gesture recognition with **MediaPipe**
- 💡 Individual control of 5 LEDs (Thumb, Index, Middle, Ring, Pinky)
- 🔄 Universal gestures to turn **all LEDs ON/OFF**
- 🌐 MQTT communication between **Python client** and **ESP32**
- 🧱 Modular and scalable design for future **smart home** applications
---

## 🖼️ Demo

![image_2025-05-27_00-38-25](https://github.com/user-attachments/assets/a1754ec2-0746-4499-9113-327430af8fe0)

---


## 🧠 How It Works

1. **Webcam** captures live video stream  
2. **MediaPipe** detects hand landmarks in real-time  
3. **Python** script analyzes gestures and publishes MQTT messages  
4. **ESP32** subscribes to MQTT topics and toggles LEDs accordingly  

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **MediaPipe & OpenCV** for gesture detection
- **ESP32** microcontroller programmed via **Arduino IDE**
- **MQTT** protocol (using **Mosquitto** broker)
- **Fritzing** for the wiring diagram

---

## ⚙️ Setup Instructions

### 1. ESP32 (Arduino Side)

- Install ESP32 board via **Arduino IDE Board Manager**
- Upload `led_control_mqtt.ino` to your ESP32
- Connect LEDs to GPIO pins (see wiring diagram)
- Set the **MQTT broker IP address** in the code (e.g., local IP of your PC or cloud broker)


### 2. Python Client (Computer Side)

Install dependencies:

```bash
pip install opencv-python mediapipe paho-mqtt
Edit gesture_control_mqtt.py to set the MQTT broker IP:
MQTT_BROKER = "your_broker_ip"
Run the script:
python gesture_control_mqtt.py

### 3. MQTT Broker
You can run Mosquitto locally or on a cloud VM:

sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto


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

🎙️ Add voice command functionality

✋ Support multi-hand recognition

📱 Create a mobile app for remote control

🏠 Integrate with platforms like Home Assistant

☁️ Use cloud MQTT brokers for remote access

---

## 🔒 Ethical and Social Impact

* 📷 All video processing is done locally — user privacy preserved
* ♿ Useful for people with mobility or speech impairments
* ⚡ Powered by energy-efficient ESP32 microcontroller
* 🌍 Designed to be inclusive, adaptable across cultures

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to improve gesture recognition, UI, or support other hardware, feel free to fork the repo.

---

## 🙋‍♂️ Authors

**Abduvahhobov Javohir**
**Mansurxojayev Xojiakbar**
Final Year Project – IoT Internship
Tashkent Turin Polytechnic University
