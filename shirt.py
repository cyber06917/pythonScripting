import argparse
import sys
from PIL import Image

try:

    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
        else:
            print("Too many command-line arguments")
        sys.exit(1)



    parser = argparse.ArgumentParser()

    #arguments
    parser.add_argument('input_img')
    parser.add_argument('output_img')

    args = parser.parse_args()

    if not args.input_img.lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit(1)

    im = Image.open(args.input_img)
    # Load the overlay image (PNG with transparency)
    overlay = Image.open("shirt.png").convert("RGBA")

    size = im.size

    overlay_resize = overlay.resize(size)

    print(im.format, im.size, im.mode)

    # Paste overlay onto background with transparency
    im.paste(overlay_resize, (0, 0), overlay_resize)

    im.save(args.output_img)



except(FileNotFoundError):
    print("File does not exsit")


