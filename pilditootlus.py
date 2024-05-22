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


#########################################################
# Leiab pildi pealt tseki piiraared ules
# sisend: - pildinimi
# väljund -
#########################################################
def leia_tseki_piirkond(pilt):
    directory = 'tsekid'

    image_path = os.path.join(directory, pilt)

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"No image found at the path: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edged = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = None
    max_area = 0
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                largest_contour = approx

    if largest_contour is None:
        raise ValueError("No bill-like contour found in the image.")

    cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 3)

    x, y, w, h = cv2.boundingRect(largest_contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Detected Bill", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pilt = "tsekk2.jpg"
leia_tseki_piirkond(pilt)
