# Design of Online Vitals Monitor by Integrating Internet of Things-enabled Sensors and Big Data Analytics

![Project Logo](logo.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to design an Online Vitals Monitor system by integrating Internet of Things (IoT)-enabled sensors and Big Data analytics. The system allows for continuous monitoring of vital signs such as heart rate, blood pressure, temperature, and oxygen levels of patients in real-time. By leveraging IoT sensors and Big Data analytics, this project provides a scalable and efficient solution for remote patient monitoring and early detection of abnormalities.

## Features
- **Real-time Monitoring**: The system enables continuous monitoring of vital signs in real-time, allowing healthcare professionals to access up-to-date information about patients' health status.
- **IoT-enabled Sensors**: The project utilizes IoT-enabled sensors to collect data from patients. These sensors can be attached to the patient's body or integrated into wearable devices.
- **Data Analytics**: The collected data is processed and analyzed using Big Data analytics techniques. This enables the system to identify patterns, detect anomalies, and generate insights for healthcare professionals.
- **Alerts and Notifications**: The system can generate alerts and notifications based on predefined thresholds or abnormal patterns in vital signs. This helps healthcare professionals respond quickly to critical situations.
- **Secure Data Transmission**: The project ensures the secure transmission of patient data over the network, maintaining privacy and confidentiality.
- **User-friendly Interface**: The system provides a user-friendly interface for healthcare professionals to visualize and interpret the collected data effectively.

## Installation
To install and run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/username/repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd repository
   ```

3. Create and activate a virtual environment with Python 3.10:

   ```bash
   python3.10 -m venv myenv
   source myenv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure the necessary environment variables. You may need to create a `.env` file and populate it with the required settings.

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application by visiting `http://localhost:8000` in your web browser.

## Usage
Once the application is running, you can perform the following actions:

1. Register a new account as a healthcare professional or log in with existing credentials.
2. Add patients to the system and associate IoT-enabled sensors with their profiles.
3. Monitor the real-time vital signs of patients on the dashboard.
4. Receive alerts and notifications for abnormal vital sign readings.
5. Access detailed reports and analytics to gain insights into patient health trends.
6. Customize system settings and thresholds according to specific requirements.

## Technologies Used
- Python 3.10
- Django Web Framework
- Internet of Things (IoT)
- Big Data Analytics
- HTML/CSS/JavaScript
- Bootstrap

## Contributing
Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5

. Submit a pull request explaining your changes.

## License
This project is licensed under the [MIT License](LICENSE).
