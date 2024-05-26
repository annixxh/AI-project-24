import pytesseract
import cv2

# NB! MUUTA OMA ARVUTIS OLEVA TESSERACT PATHIGA
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def tootle_pilti_pytesseractiga():
    img = cv2.imread('kropeeritud.png')
    tekst = pytesseract.image_to_string(img, lang="est")
    lines = tekst.splitlines()
    return lines

# Sa void need alumised meetodid teha ka chatbot.py-s, vaata ise kuidas tahad

def tootle_pytesseract_teksti(lines, dict):
    #TODO
    # leiaks pytesseracti antud tekstiks yles mis on tooted,
    # palju mis maksab ning kellele need tooted lahevad
    # praegu panin, et lines on list lausetest (string), mis pytesseract leidis tsekilt
    # dict on sonastik (voi muu andmestruktuur), kus on inimesed ja mis tooted neile lahevad voi mis nende summa on'
    # vaata ise mis sisend variablid peaks olema jne
    return None


def arvuta_summad():
    #TODO
    # arvutaks summad, kes kellele jaotub voi lihtsalt uuendab inimeste summasid vms
    # vaata ise mis sisend variablid peaks olema jne
    return None
