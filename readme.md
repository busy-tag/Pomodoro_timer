# Pomodoro Timer
## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Introduction

This Pomodoro Timer application helps you manage your work sessions effectively using the Pomodoro technique. It integrates with a Busy Tag device to display countdowns visually.

## Project Purpose

The main goal of this project is to:
	
- Provide an intuitive interface for managing work and break sessions.

- Display countdowns on a Busy Tag device.

- Automatically handle configurations and image generation for the countdown timers.

## Prerequisites

Before running the Pomodoro Timer App, ensure you have the following installed:

- Python 3.6 or higher
- `Pillow` for image generation
- `pyserial` for serial communication
- A Busy Tag device connected to your computer

## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```
   git clone https://github.com/busy-tag/pomodoro_timer.git
2. Navigate to the cloned repository:

	```
	cd pomodoro_timer
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install Pillow pyserial
	```

## Usage
1. **Execute the script:**
You can run the script from the command line:
```
python main.py
```
         
2. **Provide Drive Letter:**

	Enter the drive letter assigned to the Busy Tag device (e.g., D) when prompted.
	
3. **Set Timer Values:**
	
	Enter the desired countdown time (default is 25 minutes) and break time (default is 5 minutes).
	
4. **Start the Timer:** 

   The app will generate countdown images and start the timer sessions, displaying the countdown on the Busy Tag device.

### Example

After running the application and providing the drive letter, the app will set up the Busy Tag device and generate the necessary files. When the timer starts, you will see countdown images displayed on the Busy Tag device.

 Sample:
 
<img src="/pomodoro_sample.png" alt="Pomodoro Timer Sample" width="300" height="370"/>

### Troubleshooting

If you encounter any issues, ensure:

All required Python packages are installed correctly (Pillow and pyserial).

The font file is present in the project directory.

The drive letter is correct, and the Busy Tag device is properly connected.

You have the necessary permissions to write files to the Busy Tag device.

For any additional help, please open an issue in the repository or contact the maintainer.
