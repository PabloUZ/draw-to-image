# Draw to Image

This project allows you to draw on an image using the mouse. The image is displayed in a window and you can draw on it using the mouse. The drawing is saved to a new image file.

## How to use

1. Clone the repository

```bash
git clone origin https://github.com/PabloUZ/draw-to-image.git
```

2. Install the requirements

```bash
cd draw-to-image
pip install -r requirements.txt
```

3. Run the script

```bash
python main.py
```

4. Draw on the image

In this step, the program will display a blank image. You can draw on it using the mouse (The letter you have to draw is displayed on terminal). When you are done, press the `s` key to save the image and continue to the next.

If you don't want to save the image, press the `q` key to close the window.

The next time you run the program, it will read the images you already saved so you don't have to start from scratch.

When you finish drawing on all the images, the program will ask you to review the images one by one. You can keep the images or delete them.

If there is any image deleted, the program will ask you to draw on it again.

As soon as you finish drawing all the images and verify them, the program will generate a zip file with all the images.

## Default configuration

The default configurations are stored in the `config.py` file. You can change the values of the variables to customize the program.