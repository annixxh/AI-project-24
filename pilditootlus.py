import os
import shutil
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import cv2 as cv2


# pildi töötlemise fail - pildi leidmine, üles laadimine, pööramine ja suuruse muutmine vajadusel

#########################################################
# Pildi üles leidmine ja laadimine
# sisend: pildinimi (nt "tsekk1.jpg")
# väljund: Image tüübina pilt
#########################################################
def leia_pilt(pildinimi):
    try:
        image_path = os.path.join('tsekid', pildinimi)
        if os.path.isfile(image_path):
            print(f"Found image {pildinimi}")
            image = Image.open(image_path)
            return image
        else:
            raise FileNotFoundError(f"No image named '{pildinimi}' found in the '{pildinimi}' directory.")
    except Exception as e:
        print(e)
        return None


# lae_pilt("tsekk2.jpg")

#########################################################
# Pildi üles laadimine ja selle leidmine leia_pilt() meetodi abil
# sisend: -
# väljund: Image tüübina pilt, mis laeti kasutja arvutist üles
#########################################################
def lae_ules_pilt():
    # aken, kus üles laadida pilti, vb muuta GUI-d
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )

    if file_path:
        try:
            image_name = os.path.basename(file_path)
            directory = 'tsekid'
            os.makedirs(directory, exist_ok=True)
            destination = os.path.join(directory, image_name)
            shutil.move(file_path, destination)
            image = leia_pilt(image_name)
            if image:
                image.show()
            else:
                raise FileNotFoundError(
                    f"Failed to load the image named '{image_name}' from the '{directory}' directory.")
        except Exception as e:
            print(e)
    else:
        print("No file selected.")

# lae_ules_pilt()

# pilt = "tsekk2.jpg"
