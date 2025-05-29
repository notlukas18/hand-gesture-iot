#include <WiFi.h>
#include <PubSubClient.h>

// WiFi credentials
const char* ssid = "Wifi";             // <-- your Wi-Fi SSID
const char* password = "123456789h";   // <-- your Wi-Fi password

// MQTT Broker settings (your VM IP)
const char* mqtt_server = "34.27.113.8";
const int mqtt_port = 1883;
const char* mqtt_user = "pablo";
const char* mqtt_pass = "idunno";

// GPIO pins for LEDs
const int thumbLedPin = 27; 
const int indexLedPin = 26; 
const int middleLedPin = 25;
const int ringLedPin = 33; 
const int pinkyLedPin = 32;

WiFiClient espClient;
PubSubClient client(espClient);

// Turn LEDs ON or OFF based on finger
void controlLed(const String &finger, bool state) {
  if (finger == "thumb") digitalWrite(thumbLedPin, state ? HIGH : LOW);
  else if (finger == "index") digitalWrite(indexLedPin, state ? HIGH : LOW);
  else if (finger == "middle") digitalWrite(middleLedPin, state ? HIGH : LOW);
  else if (finger == "ring") digitalWrite(ringLedPin, state ? HIGH : LOW);
  else if (finger == "pinky") digitalWrite(pinkyLedPin, state ? HIGH : LOW);
}

// Handle received MQTT message
void callback(char* topic, byte* payload, unsigned int length) {
  String message;
  for (unsigned int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.print("Message arrived on topic: ");
  Serial.println(topic);
  Serial.print("Message: ");
  Serial.println(message);

  String topicStr = String(topic);
  if (topicStr.startsWith("hand/led/")) {
    String finger = topicStr.substring(9);
    bool state = (message == "on");
    controlLed(finger, state);
  }
}

// MQTT reconnection
void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP32Client", mqtt_user, mqtt_pass)) {
      Serial.println("connected");
      client.subscribe("hand/led/thumb");
      client.subscribe("hand/led/index");
      client.subscribe("hand/led/middle");
      client.subscribe("hand/led/ring");
      client.subscribe("hand/led/pinky");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(thumbLedPin, OUTPUT);
  pinMode(indexLedPin, OUTPUT);
  pinMode(middleLedPin, OUTPUT);
  pinMode(ringLedPin, OUTPUT);
  pinMode(pinkyLedPin, OUTPUT);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
  Serial.println(WiFi.localIP());

  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
