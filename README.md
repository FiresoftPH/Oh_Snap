# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Install the following libraries required to run the software

```bash
sudo apt-get install python-opencv python3-opencv opencv-data
sudo pip3 install mediapipe-rpi3
sudo pip3 install mediapipe-rpi4
sudo pip3 install gtts
sudo apt install mpg321
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

TBA
