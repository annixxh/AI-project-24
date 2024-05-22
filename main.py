import os
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

def lae_pilt(pildinimi):
    path = f"./tsekid/{pildinimi}"
    image = Image.open(path)
    image.show()


lae_pilt("tsekk1")
