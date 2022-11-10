# Oh Snap!

Oh Snap! is a mini PhotoBooth Project that uses Rasperry Pi 4B as the main computing device. The Raspberry Pi operating system is Raspberry Pi Legacy OS (Debian 10 Buster) for an optimal library support. The main software is Python based with open-sourced libraries such as Google Mediapipe, OpenCV and Customtkinter. (Linked to their respective repositories will be listed in the credits section. This project requires specific hardware requirements which will be listed below.

## Hardware used in the project

- Raspberry Pi 4B (4GB or more RAM)
- A 32GB SD Card with Raspberry Pi OS Legacy installed (Debian Buster)
- Pi Camera HQ Module (12MP Sony IMX477R)
- ICE Tower CPU Cooler or any active cooling solution
- 10.1" Touch Enabled Screen
- Wooden Enclosure (Can be different according to your design

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
sudo pip3 install Flask
```

## Usage

```terminal
TBA
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

TBA
