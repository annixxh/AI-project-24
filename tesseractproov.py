import pytesseract
from PIL import Image
import cv2

# see fail on selleks, et naha kas pytesseract tootab
# enne peab programmi labi jooksutama, et kropeeritud.png fail oleks olemas
# import pytesseract peaks tootama automaatselt, kui oled conda cmd kaudu installinud pytesseracti
# vaata File -> Settings -> Project: AI-project-24 -> Python interpreter
# kui su interpreter on anaconda, siis installi pytesseract conda kaudu
# kui su interpreter ei ole anaconda vaid muu python, siis pip-i kaudu
# pytesseracti kasutamise juhend: https://pypi.org/project/pytesseract/


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


print(pytesseract.image_to_string(Image.open('kropeeritud.png')))
print("**************************************************************'")

print(" EESTI KEELE KONTROLL ")
print(pytesseract.get_languages(config=''))

img = cv2.imread("kropeeritud.png")
print(pytesseract.image_to_string(img, lang="est"))
