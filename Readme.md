# Audio and Video Playback with Random Device Selection

## Overview
This Python program allows you to play audio or video using a random selection of audio output devices. It utilizes the `pyaudio`, `sounddevice`, and `soundfile` libraries to provide flexibility in choosing the audio devices for playback.

## Program Features
- Select between audio and video playback.
- Choose specific devices for output from a random selection.
- Enjoy media playback using the chosen audio output devices.

## Prerequisites
- Python 3.x
- Required Python packages: `pyaudio`, `sounddevice`, `soundfile`

## Usage
1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the program's directory.

3. Run the program with the following command:

```python
python your_program.py -t [type] -f [file] -d [device_indices]
```

### Replace the placeholders:
- `[type]`: Specify the media type (`song` for audio or `vid` for video).
- `[file]`: Provide the path to the audio or video file you want to play.
- `[device_indices]`: Enter a comma-separated list of device indices from the provided list.

4. The program will play the selected media on the specified audio output devices.

## Example Usage
- To play an audio file on random devices:


```python
python your_program.py -t song -f audio.mp3 -d 1,3,5
```

- To play a video (not yet implemented):

```python
python your_program.py -t vid -f video.mp4 -d 2,4
```


## License
This program is open-source and released under the [MIT License](LICENSE).

## Author
- [Varun S V](varunsv077@gmail.com)

