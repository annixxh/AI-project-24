import pytesseract
import cv2
import re

# NB! MUUTA OMA ARVUTIS OLEVA TESSERACT PATHIGA
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def tootle_pilti_pytesseractiga():
    tekst1="""Kilekott MAXIMA EPI

0.10A
Pet pudel 1,5] 0.08 N
Vesi AURA Fruit 0.94 A
J hkel FAZ
azeri Hele peenleib, 0.83 A
Spagetid BIG 4009 0.39 A
Keeduvorst Doktori NÕO 250g 1.16 4
Kodujuust EKSTRA 6% 0.84 A
Mandariin väike, ka
1.09 X 1.316 KG 1.43 4
Allahindlus -0.13 4
Kohup.kreem FARMI vaarika 0.57 A
Kohup.kreem FARMI vaarika 0.57 4
Kohup.kreem FARMI vaarika 0.57 4
Kodujuust EKSTRA 6% 0.84 A
Majonees Provansaal JAANI 40% 2.274
Hapukoor ARMAS 20% 500g 0.63 A
Hapukoor ARMAS 20% 500g 0.63 A
Või ARMAS 82% 1809 0.95 A
Või ARMAS 82% 1609 0.95 4
Või ARMAS 82% 1809 0.95 4"""
    img = cv2.imread('kropeeritud.png')
    tekst = pytesseract.image_to_string(img, lang="est")
    #print(tekst)
    # Split the input text into lines
    lines = tekst1.split("\n") ####muuta siin tekst1 ära

    # Initialize the list to hold the parsed data
    parsed_list = []

    # Helper function to extract price and name
    def extract_price_name(parts):
        if len(parts) < 2:
            return None, None
        try:
            price = float(parts[-2])
            name = " ".join(parts[:-2]).strip()
            return name, price
        except ValueError:
            return None, None

    # Iterate over the lines and parse the data
    index = 1
    buffer = []
    for i, line in enumerate(lines):
        if line.strip() == "":
            continue
        parts = line.rsplit(' ', 2)
        name, price = extract_price_name(parts)
        if line.startswith("Allahindlus"):
            # Remove the discount from the previous entry
            if parsed_list:
                discount = float(parts[-2])
                parsed_list[-1][2] += discount
        elif name is not None and price is not None:
            if buffer:
                name = " ".join(buffer) + " " + name
                buffer = []
            parsed_list.append([index, name, price])
            index += 1
        else:
            buffer.append(line.strip())

    # Handle any remaining buffered lines
    if buffer:
        parts = buffer[-1].rsplit(' ', 2)
        name, price = extract_price_name(parts)
        if name is not None and price is not None:
            buffer.pop()
            name = " ".join(buffer) + " " + name
            parsed_list.append([index, name, price])
    print(parsed_list)
    return parsed_list

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
