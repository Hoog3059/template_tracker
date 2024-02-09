# Template Tracker

Template Tracker is a small utility to track the position on a template in a video or set of videos. The program uses [OpenCV template matching](https://docs.opencv.org/5.x/d4/dc6/tutorial_py_template_matching.html).

## Installation

Install necessary packages:
```bash
> pip install -r requirements.txt
```

## Running

Run the program:
```bash
> pythom tracker.py
┌─────────────────────┐
│                     │
│ Welcome to Tracker! │
│                     │
│    Version 1.0.0    │
│                     │
└─────────────────────┘
Please provide the root directory containing the video and settings files.
Root directory > 
```

The program will search the root directory for video files and `tracker.json` files. These files contain the template that should be used with those videos. For all videos and corresponding `tracker.json` files, the program will track the corresponding template for each video and output a `{video_name}.csv` in the same folder as the video with three column: frame_nr, y_from_top, x_from_left.

## Folder structure and contents of `tracker.json`

tracker.json :
```json
{
    "template": "/path/to/template.png",
}
```

So a folder structure may look like:
```
.
├── uses_template_1/
│   ├── video1.mp4
│   ├── video2.mp4
│   └── tracker.json
├── uses_template_2/
│   ├── video3.mp4
│   └── tracker.json
└── templates/
    ├── template_1.png
    └── template_2.png
```

Here `uses_template_1/tracker.json`:
```json
{
    "template": "/templates/template_1.png",
}
```