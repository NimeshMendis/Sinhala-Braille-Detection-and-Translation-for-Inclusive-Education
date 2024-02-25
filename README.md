# Sinhala-Braille-Detection-and-Translation-for-Inclusive-Education

A two way translation system between physical Sinhalla and English braille and plain text. Developed as a final year project at SLTC Research University.

## Features

- Braille to Text Translation
- Text to Braille Translation
- Tactile Output for Braille
- Support for Sinhala and English Braille Alphabest

## Setting up Development Environment for the Desktop Application

Python 3.10 Recommended.

```bash
pip install -r requirements.txt
```

## Setting up Development Environment for the Braille Display in Raspberry Pi

Developed with a Raspberry Pi 4. But any model with PWM output should work.

```bash
sudo apt-get install python-smbus
```

```bash
sudo apt-get install i2c-tools
```

```bash
pip install adafruit-circuitpython-servokit
```

```bash
pip install pyrebase4
```


