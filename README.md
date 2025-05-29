# ✋🤖 Hand Gesture Controlled IoT System

**ESP32 + Python + OpenCV + MediaPipe + MQTT**

This final-year project showcases a **smart, contactless interface** that enables users to control multiple LEDs using hand gestures. Leveraging **Computer Vision** and **IoT**, it offers a modern, accessible, and touchless control solution for smart environments and home automation.

---

## 🚀 Key Features

* 🖐️ **Real-time hand gesture recognition** using MediaPipe
* 💡 **Individual control** of five LEDs (Thumb, Index, Middle, Ring, Pinky)
* 🔄 **Universal gestures** to toggle all LEDs ON/OFF
* 🌐 **MQTT communication** between Python client and ESP32
* 🧱 Modular, scalable design for future **smart home integration**

---

## 🖼️ Demo Preview

![Demo Screenshot](https://github.com/user-attachments/assets/a1754ec2-0746-4499-9113-327430af8fe0)

---

## 🧠 System Overview

1. A **webcam** captures the live video stream
2. **MediaPipe** detects hand landmarks in real time
3. A **Python script** processes gestures and sends MQTT messages
4. The **ESP32** microcontroller receives the messages and toggles LEDs accordingly

---

## 🛠️ Tech Stack

* **Python 3.11+**
* **MediaPipe & OpenCV** for gesture detection
* **ESP32** programmed via **Arduino IDE**
* **MQTT** protocol with **Mosquitto broker**
* **Fritzing** for circuit design and wiring diagrams

---

## 🖥️ Getting Started

### 1. Python Client (Computer Side)

Install the required dependencies:

```bash
pip install opencv-python mediapipe paho-mqtt
```

Edit the `gesture_control_mqtt.py` file to specify your MQTT broker IP:

```python
MQTT_BROKER = "your_broker_ip"
```

Run the script:

```bash
python gesture_control_mqtt.py
```

---

### 2. MQTT Broker Setup

You can install Mosquitto locally or on a cloud-based virtual machine:

```bash
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto
```

---

## ✋ Supported Hand Gestures

| Gesture          | Action                 |
| ---------------- | ---------------------- |
| All fingers up   | Turn **ALL LEDs ON**   |
| All fingers down | Turn **ALL LEDs OFF**  |
| Thumb only up    | Turn ON **Yellow LED** |
| Index only up    | Turn ON **Red LED**    |
| Middle only up   | Turn ON **Green LED**  |
| Ring only up     | Turn ON **Blue LED**   |
| Pinky only up    | Turn ON **White LED**  |

---

## 📈 Future Enhancements

* 🎙️ Add **voice command** functionality
* ✋ Enable **multi-hand gesture** recognition
* 📱 Build a **mobile app** for remote access
* 🏠 Integrate with platforms like **Home Assistant** or **Google Home**

---

## 🔒 Ethical & Social Impact

* 📷 All video processing is performed **locally** — ensuring **user privacy**
* ♿ Highly beneficial for users with **mobility or speech impairments**
* ⚡ Uses an **energy-efficient ESP32** for minimal power consumption
* 🌍 Designed to be **inclusive, adaptable**, and globally applicable

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

We welcome pull requests!
If you'd like to improve gesture recognition, expand hardware compatibility, or enhance the interface, feel free to fork the repo and contribute.

---

## 👥 Authors

* **Abduvahhobov Javohir** – Software Development (Python, OpenCV, MQTT)
* **Mansurxojayev Xojiakbar** – Hardware Design (ESP32, Circuit Wiring)

> Final Year Project — IoT Internship
> Tashkent Turin Polytechnic University

