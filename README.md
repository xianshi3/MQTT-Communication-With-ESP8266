# MQTT Communication with ESP8266

## Project Overview
This project demonstrates how to establish MQTT communication using the ESP8266 microcontroller. It connects to a Wi-Fi network, subscribes to a specific MQTT topic, and displays received messages on an OLED screen. The project utilizes MicroPython for programming the ESP8266 and includes functionalities for both receiving and sending messages via MQTT.

## File Descriptions

### src/main.py
This is the main script for the project. It includes the following functionalities:
- **Wi-Fi Connection**: The `WIFI_Connect` function connects the ESP8266 to a specified Wi-Fi network and displays the network information on the OLED screen.
- **MQTT Client**: The script initializes an MQTT client using the `MQTTClient` class, connects to the MQTT broker, and subscribes to a specified topic.
- **Message Handling**: The `MQTT_callback` function processes incoming messages and displays them on the OLED screen.
- **Periodic Tasks**: The script uses a timer to periodically check for incoming MQTT messages and send messages to the subscribed topic.

### README.md
This file contains the project documentation, including setup instructions, usage guidelines, and any necessary information for users to understand and run the project.

### requirements.txt
This file lists the required libraries and dependencies for the project, ensuring that users can install the necessary packages to run the code successfully.

## Usage
1. Clone the repository to your local machine.
2. Install the required libraries listed in `requirements.txt`.
3. Modify the Wi-Fi credentials in the `main.py` file.
4. Upload the `main.py` script to the ESP8266.
5. Run the script to start the MQTT communication.

## Conclusion
This project serves as a practical example of using MQTT with the ESP8266, showcasing how to connect to a Wi-Fi network, subscribe to topics, and display messages on an OLED screen. It can be further expanded to include additional features such as publishing messages or integrating with other IoT devices.
