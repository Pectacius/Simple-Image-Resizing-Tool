# Image Resizer

Simple GUI that allows for the resizing of various image formats

## Description
A tkinter GUI that uses pillow to resize images based on input length and width ratios

#### Supported Image Formats

Currently, the file search function filters, and the file save options are:
 - `.bmp`
 - `.jpg / .jpeg`
 - `.png`
 - `.svg`
 - `.tiff`
 
 Pillow can support more formats, so feel free to add more file formats to the `valid_file_types` tuple in `main.py`:
 
 ```
valid_file_types = (("Bitmap files", "*.bmp*"),
                        ("JPEG files", "*.jpg*"),
                        ("PNG files", "*.png*"),
                        ("SVG files", "*.svg*"),
                        ("TIFF files", "*.tiff*"))
```

## Setup
1. Clone repository and run `pipenv sync` to install dependencies in new environment
2. run `main.py`

## Usage
![Application](info/app.PNG)
- `Browse Files` allows an image file to be selected
- `View Loaded` opens the selected image in default image viewer
- Type x and y resize ratios in the boxes for `X Ratio` and `Y Ratio` respectively
- Press `Resize` to apply the ratios to the loaded image
- `Loaded X Size`, `Loaded Y Size`, `Resized X Size` and `Resized Y Size` displays the pixels of the loaded and edited image respectively
- Preview the resized image in default image viewer with `View Edited`
- Save the edited image with `Save`

#### Note
![File](info/selectfile.PNG)

Use the dropdown to change the type of file being searched when selecting an image to be opened
