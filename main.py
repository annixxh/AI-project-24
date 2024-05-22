import os
import shutil
from PIL import Image


# 1. Sisestad pildi
# 2. võibolla vaja image töötlust
# 2. programm loeb sisse pildi ning küsib, mida teha (kuidas jagada)
# 3. programm loeb pildi pealt tooted ning nende hinnad
# 4. vastavalt kasutaja soovile jaotab programm automaatselt ära, kes kui palju peab maksma
#
# pildi pealt character ja sõnade recognition - tesseract
#
# juturobot, küsib mida teha ning kui ei tea täpselt mida teha siis küsib üle
#
# Et pildilt arusaada, mis toodet kuhu jaotada, peab inimene ütlema tšeki pealt,
# kas toote järjekorranumbri või siis toote nimest vähemalt mingi osa.
#
# Kui juturobot ei leia täpselt, siis küsib üle, kuni saab õige

#########################################################
# Pildi üles leidmine ja laadimine
# sisend: pildinimi (nt "tsekk1.jpg")
# väljund: Image tüübina pilt
#########################################################
def lae_pilt(pildinimi):
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


lae_pilt("tsekk2.jpg")
