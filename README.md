# Oh Snap!

Oh Snap! is a mini PhotoBooth Project that uses Rasperry Pi 4B as the main computing device. The Raspberry Pi operating system is Raspberry Pi Legacy OS (Debian 10 Buster) for an optimal library support. The main software is Python based with free to use open-sourced libraries such as Google Mediapipe, OpenCV and Customtkinter. (Linked to their respective repositories will be listed in the credits section. This project requires specific hardware requirements which will be listed below.

## Hardware used in the project

- Raspberry Pi 4B (4GB or more RAM)
- A 32GB SD Card with Raspberry Pi OS Legacy installed (Debian Buster)
- Pi Camera HQ Module (12MP Sony IMX477R)
- ICE Tower CPU Cooler or any active cooling solution
- 10.1" Touch Enabled Screen
- Wooden Enclosure (Can be different according to your design

## Design

![](https://github.com/FiresoftPH/Oh_Snap/blob/master/Pictures/Design.png)

The design of the hardware includes a touch screen monitor at the bottom of the box, a camera at the center where the result of the image would not have a too high or too low angle of the user’s face, and a LED above the camera to brighten up the user’s face for the filter process in the photo taking process.

## Installation

Install the following libraries required to run the software

Update your Raspberry Pi OS
```bash
sudo apt-get update && sudo apt-get upgrade
```

MediaPipe and OpenCV
```bash
sudo apt-get install python-opencv python3-opencv opencv-data
```
```bash
sudo pip3 install mediapipe-rpi3
```
```bash
sudo pip3 install mediapipe-rpi4
```
```bash
sudo pip3 install gtts
```
```bash
sudo apt install mpg321
```

CustomTkinter
```bash
sudo pip3 install customtkinter
```

Pillow (For Pictures)
```bash
sudo pip3 install Pillow
```

Flask
```bash
sudo pip3 install Flask==2.0.3
```

Jinja2
```bash
sudo pip3 install Jinja2==X.XX
```

## Usage

Run the User_Interface.py and configure all the directories according to your directories of the code. Later revisions to the code that doesn't require this modification will be provided at a later revision.

## Contributors

- Pattarapark Chutisamoot - User Interface, Major Camera Software and Major Code Integration
- Puttipong Aunggulsant - Webserver/Website, Minor Camera Software and Minor Code Integration
- Pimchanok Payungwataseth - Hardware Design/Assembling, UI Designer and Art Designer
- Phattarada Limsuchaiwat - Picture Processing Software, UI Designer and Art Designer

## Credits

- Google Mediapipe - https://google.github.io/mediapipe/
- Customtkinter - https://github.com/TomSchimansky/CustomTkinter
- OpenCV - https://opencv.org/
- Flask - https://github.com/pallets/flask
- Jinja2 - https://github.com/pallets/jinja
- Pillow (PIL) - https://pillow.readthedocs.io/en/stable/index.html

## License

TBA
